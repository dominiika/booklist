from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, View

from .filters import BookFilter
from .forms import AuthorModelForm, BookModelForm, FetchBookForm
from .models import Author, Book
from .services import NOT_SPECIFIED_INFO, BookApiFetcher


class BookListView(ListView):
    template_name = "book/index.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["not_specified_str"] = NOT_SPECIFIED_INFO
        context["filter"] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BookCreateView(CreateView):
    template_name = "book/form.html"
    model = Book
    form_class = BookModelForm

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context["btn_text"] = "Save"
        context["title"] = "Add a book"
        context["add_author"] = True
        return context

    def form_valid(self, form):
        form.save()
        return redirect("book-list")


class BookUpdateView(UpdateView):
    template_name = "book/form.html"
    model = Book
    form_class = BookModelForm

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data(**kwargs)
        context["btn_text"] = "Save"
        context["title"] = "Update the book"
        context["add_author"] = True
        return context

    def form_valid(self, form):
        form.save()
        return redirect("book-list")


class FetchBooksView(View):
    form_class = FetchBookForm
    initial = {"key": "value"}
    template_name = "book/fetch.html"
    fetcher = BookApiFetcher()

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {"form": form, "btn_text": "Fetch"}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {"form": form, "btn_text": "Fetch"}
        if form.is_valid():
            title = (
                form.cleaned_data["title"] if form.cleaned_data["title"] != "" else None
            )
            author = (
                form.cleaned_data["author"]
                if form.cleaned_data["author"] != ""
                else None
            )
            key_word = (
                form.cleaned_data["key_word"]
                if form.cleaned_data["key_word"] != ""
                else None
            )
            books = self.fetcher.search_by(
                key_word=key_word, title=title, author=author
            )
            context["books"] = books
            self.request.session["books"] = books
        return render(request, self.template_name, context)


def validate_fields(data):
    for k, v in data.items():
        if v == NOT_SPECIFIED_INFO:
            data[k] = None
    return data


def handle_pub_date_data(book_data):
    pub_date = book_data.get("pub_date")
    try:
        int(pub_date)
    except ValueError:
        book_data["pub_date"] = pub_date.split("-")[0] if pub_date else None
    return book_data


def handle_author_data(book_data):
    author_name = book_data.pop("author")
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        author = Author.objects.create(name=author_name) if author_name else None
    return author


def save_book(request, book_id):
    books = request.session["books"]
    book_data = [book for book in books if book["temp_id"] == book_id][0]
    book_data.pop("temp_id")
    book_data = validate_fields(book_data)

    author = handle_author_data(book_data)
    book_data = handle_pub_date_data(book_data)

    Book.objects.create(author=author, **book_data)
    return redirect("/books")


class AuthorCreateView(CreateView):
    template_name = "book/form.html"
    model = Author
    form_class = AuthorModelForm

    def get_context_data(self, **kwargs):
        context = super(AuthorCreateView, self).get_context_data(**kwargs)
        context["btn_text"] = "Save"
        context["title"] = "Add an author"
        return context

    def form_valid(self, form):
        form.save()
        return redirect("book-list")
