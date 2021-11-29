from book.models import Book
from django_filters import rest_framework as filters


class BookApiFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            "title": ["icontains"],
            "author__name": ["icontains"],
            "pub_language": ["icontains"],
            "pub_date": ["gt", "lt"],
        }
