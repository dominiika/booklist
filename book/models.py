import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.PositiveIntegerField(
        default=current_year(),
        validators=[MinValueValidator(1800), max_value_current_year],
        blank=True,
        null=True,
    )
    isbn = models.CharField(max_length=255, blank=True, null=True)
    page_count = models.PositiveIntegerField(blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)
    pub_language = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
