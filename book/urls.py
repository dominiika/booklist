from django.urls import path

from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book-list"),
    path("create/", views.BookCreateView.as_view(), name="book-create"),
    path("update/<int:pk>/", views.BookUpdateView.as_view(), name="book-update"),
    path("fetch/", views.FetchBooksView.as_view(), name="fetch"),
    path("save/<int:book_id>/", views.save_book, name="save"),
]
