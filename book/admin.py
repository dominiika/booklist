from django.contrib import admin

from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "pub_date",
        "isbn",
        "page_count",
        "cover_url",
        "pub_language",
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
