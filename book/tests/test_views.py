from django.test import TestCase
from django.urls import reverse

from book.models import Author, Book
from book.services import NOT_SPECIFIED_INFO
from book.views import handle_pub_date_data, validate_fields


class TestViews(TestCase):
    def setUp(self):
        self.books_data = [
            {
                "author": "Oscar Wilde",
                "cover_url": "http://books.google.com/test123",
                "isbn": "1551111268",
                "page_count": 280,
                "pub_date": "1998",
                "pub_language": "not specified",
                "temp_id": 0,
                "title": "The Picture of Dorian Gray",
            }
        ]

    def _create_book(self, **kwargs):
        return Book.objects.create(**kwargs)

    def test_book_list_view(self):
        self._create_book(title="Book1")
        self._create_book(title="Book2")

        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["book_list"]), 2)

    def test_book_create_view(self):
        data = {
            "title": "Book1",
            "pub_date": "2021",
            "isbn": "1234-5678-9012-0000",
        }

        url = reverse("book-create")
        response = self.client.post(url, data)

        book = Book.objects.get(title=data["title"])

        self.assertEqual(response.status_code, 302)
        self._assert_book_has_correct_fields(book, data)

    def _assert_book_has_correct_fields(self, book, data):
        self.assertEqual(book.title, data["title"])
        self.assertEqual(book.pub_date, int(data["pub_date"]))
        self.assertEqual(book.isbn, data["isbn"])

    def test_book_update_view(self):
        book = self._create_book(
            title="Book1", pub_date=2020, isbn="abcd-1111-1111-2222"
        )
        new_data = {
            "title": book.title,
            "pub_date": "2021",
            "isbn": "1234-5678-9012-0000",
        }

        url = reverse("book-update", args=[book.id])
        response = self.client.post(url, new_data)

        book.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self._assert_book_has_correct_fields(book, new_data)

    def test_save_book_view(self):
        author = self._create_author(self.books_data[0]["author"])
        session = self.client.session
        session["books"] = self.books_data
        session.save()

        url = reverse("save", args=[self.books_data[0]["temp_id"]])
        response = self.client.post(url)

        book = Book.objects.get(title=self.books_data[0]["title"])

        self._assert_book_has_correct_fields(book, self.books_data[0])
        self.assertEqual(response.status_code, 302)
        self.assertEqual(book.author, author)

    def _create_author(self, name):
        return Author.objects.create(name=name)

    def test_save_book_view_adds_new_author_if_not_exist(self):
        session = self.client.session
        session["books"] = self.books_data
        session.save()

        url = reverse("save", args=[self.books_data[0]["temp_id"]])
        response = self.client.post(url)

        book = Book.objects.get(title=self.books_data[0]["title"])
        author = Author.objects.get(name=self.books_data[0]["author"])

        self.assertEqual(response.status_code, 302)
        self._assert_book_has_correct_fields(book, self.books_data[0])
        self.assertEqual(author.name, self.books_data[0]["author"])
        self.assertEqual(book.author, author)

    def test_saves_pub_date_in_correct_format(self):
        data = {"title": "test title", "pub_date": "2021-04-04"}
        expected_pub_date = "2021"

        result = handle_pub_date_data(data)

        self.assertEqual(result["pub_date"], expected_pub_date)

    def test_validates_fields(self):
        data = {
            "title": "test title",
            "author": NOT_SPECIFIED_INFO,
        }
        expected_result = {
            "title": "test title",
            "author": None,
        }

        result = validate_fields(data)

        self.assertEqual(result, expected_result)
