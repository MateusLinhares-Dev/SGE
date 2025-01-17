from django.contrib import admin  # type: ignore
from django.shortcuts import render
from django.urls import include, path  # type: ignore


def ren(request):

    return render(request, "base.html", status=200)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", ren),  # type: ignore
    path("", include("brands.urls")),
]
