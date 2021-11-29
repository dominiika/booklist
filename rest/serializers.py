from book import models
from book.models import Author
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    author_name = serializers.CharField(source="author", read_only=True)

    class Meta:
        model = models.Book
        fields = (
            "id",
            "title",
            "author",
            "author_name",
            "pub_date",
            "isbn",
            "page_count",
            "cover_url",
            "pub_language",
        )
