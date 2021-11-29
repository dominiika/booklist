from unittest import mock

from django.test import TestCase

from book.services import BookApiFetcher


class BookAPIFetcherTests(TestCase):
    def setUp(self):
        self.mocked_api_response = self._preapre_mocked_api_response()
        self.expected_response = self._prepare_expected_response()

    @mock.patch("book.services.requests.get")
    def test_fetches_and_returns_correct_data(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = self.mocked_api_response
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        fetcher = BookApiFetcher()
        result = fetcher.search_by(title="The Picture of Dorian Gray")

        self.assertEqual(result, self.expected_response)

    def _preapre_mocked_api_response(self):
        mocked_api_response = {
            "kind": "books#volumes",
            "totalItems": 1,
            "items": [
                {
                    "volumeInfo": {
                        "title": "The Picture of Dorian Gray",
                        "authors": ["Oscar Wilde"],
                        "publisher": "Broadview Press",
                        "publishedDate": "1998-02-23",
                        "industryIdentifiers": [
                            {"type": "ISBN_10", "identifier": "1551111268"},
                            {"type": "ISBN_13", "identifier": "9781551111261"},
                        ],
                        "pageCount": 280,
                        "imageLinks": {
                            "smallThumbnail": "http://books.google.com/test123",
                            "thumbnail": "http://books.google.com/test123",
                        },
                        "canonicalVolumeLink": "https://books.google.com/books/about/The_Picture_of_Dorian_Gray.html",
                    },
                }
            ],
        }
        return mocked_api_response

    def _prepare_expected_response(self):
        expected_response = [
            {
                "author": "Oscar Wilde",
                "cover_url": "http://books.google.com/test123",
                "isbn": "1551111268",
                "page_count": 280,
                "pub_date": "1998-02-23",
                "pub_language": "not specified",
                "temp_id": 0,
                "title": "The Picture of Dorian Gray",
            }
        ]
        return expected_response
