from django.test import TestCase
from django.urls import resolve, reverse

from rest import views


class UrlsTests(TestCase):
    def test_book_list_api_view(self):
        url = reverse("book-list-rest")

        self.assertEqual(
            resolve(url).func.__name__, views.BookListAPIView.as_view().__name__
        )
