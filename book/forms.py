from django import forms

from .models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "pub_date", "isbn", "page_count", "cover_url")


class FetchBookForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    author = forms.CharField(max_length=100, required=False)
    key_word = forms.CharField(max_length=100, required=False, label="Any word")
