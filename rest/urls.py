from django.urls import path

from rest import views

urlpatterns = [path("books/", views.BookListAPIView.as_view(), name="book-list-rest")]
