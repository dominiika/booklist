import requests

NOT_SPECIFIED_INFO = "not specified"
FIELD_NAMES_MAP = {"title": "intitle:", "author": "inauthor:", "key_word": ""}
API_URL = "https://www.googleapis.com/books/v1/volumes"


class BookApiFetcher:
    def __init__(self):
        self.url = API_URL

    def search_by(self, **kwargs):
        query = "?q="
        for k, v in kwargs.items():
            query = self._prepare_query(k, v, query)
        print(query)
        result = self._fetch_result(query)
        return result

    def _prepare_query(self, k, v, query):
        if v:
            query += f"{FIELD_NAMES_MAP[k]}{v}+"
        return query

    def _fetch_result(self, query):
        response = requests.get(f"{self.url}{query}")
        books = self._prepare_data(response.json())
        return books

    def _prepare_data(self, response):
        books = []
        for i, item in enumerate(response["items"]):
            volume_info = item["volumeInfo"]
            authors = volume_info.get("authors")
            industry_identifiers = volume_info.get("industryIdentifiers")
            image_links = volume_info.get("imageLinks")
            data = {
                "temp_id": i,
                "title": volume_info.get("title", NOT_SPECIFIED_INFO),
                "author": authors[0] if authors else NOT_SPECIFIED_INFO,
                "pub_date": volume_info.get("publishedDate", NOT_SPECIFIED_INFO),
                "page_count": volume_info.get("pageCount", NOT_SPECIFIED_INFO),
                "pub_language": volume_info.get("language", NOT_SPECIFIED_INFO),
                "isbn": industry_identifiers[0]["identifier"]
                if industry_identifiers
                else NOT_SPECIFIED_INFO,
                "cover_url": image_links.get("thumbnail")
                if image_links
                else NOT_SPECIFIED_INFO,
            }
            books.append(data)
        return books
