from django.test import TestCase
from django.urls import resolve, reverse

from book import views


class UrlsTests(TestCase):
    def test_book_list_view(self):
        url = reverse("book-list")

        self.assertEqual(
            resolve(url).func.__name__, views.BookListView.as_view().__name__
        )

    def test_book_create_view(self):
        url = reverse("book-create")

        self.assertEqual(
            resolve(url).func.__name__, views.BookCreateView.as_view().__name__
        )

    def test_book_update_view(self):
        book_id = 1
        url = reverse("book-update", kwargs={"pk": book_id})

        self.assertEqual(
            resolve(url).func.__name__, views.BookUpdateView.as_view().__name__
        )

    def test_fetch_view(self):
        url = reverse("fetch")

        self.assertEqual(
            resolve(url).func.__name__, views.FetchBooksView.as_view().__name__
        )

    def test_save_book_view(self):
        book_id = 1
        url = reverse("save", kwargs={"book_id": book_id})

        self.assertEqual(resolve(url).func.__name__, views.save_book.__name__)

    def test_author_create_view(self):
        url = reverse("author-create")

        self.assertEqual(
            resolve(url).func.__name__, views.AuthorCreateView.as_view().__name__
        )
