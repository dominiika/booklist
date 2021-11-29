from book.models import Book
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from rest.serializers import BookSerializer


class BookListApiViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_returns_book_list_api_view(self):
        self._create_book(title="Book1")
        self._create_book(title="Book2")

        url = reverse("book-list-rest")
        response = self.client.get(url)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def _create_book(self, title="Test title"):
        return Book.objects.create(title=title)
