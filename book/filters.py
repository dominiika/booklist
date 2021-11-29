import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            "title": ["icontains"],
            "author__name": ["icontains"],
            "pub_language": ["icontains"],
            "pub_date": ["gt", "lt"],
        }
