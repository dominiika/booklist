from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book-list"),
    path("create-book/", views.BookCreateView.as_view(), name="book-create"),
    path("update-book/<int:pk>/", views.BookUpdateView.as_view(), name="book-update"),
    path("fetch-books/", views.FetchBooksView.as_view(), name="fetch-books"),
    path("save-book/<int:book_id>/", views.save_book, name="save-book"),
    path("create-author/", views.AuthorCreateView.as_view(), name="author-create"),
]
