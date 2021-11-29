from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book-list"),
    path("create-book/", views.BookCreateView.as_view(), name="book-create"),
    path("update-book/<int:pk>/", views.BookUpdateView.as_view(), name="book-update"),
    path("fetch/", views.FetchBooksView.as_view(), name="fetch"),
    path("save/<int:book_id>/", views.save_book, name="save"),
    path("create-author/", views.AuthorCreateView.as_view(), name="author-create"),
]
