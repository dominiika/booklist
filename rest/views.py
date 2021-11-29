from book import models
from rest_framework.generics import ListAPIView

from rest import serializers
from rest.filters import BookApiFilter


class BookListAPIView(ListAPIView):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
    filterset_class = BookApiFilter
