from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("books/", include("book.urls")),
    path("", RedirectView.as_view(url="/books")),
    path("api/v1/", include("rest.urls")),
]
