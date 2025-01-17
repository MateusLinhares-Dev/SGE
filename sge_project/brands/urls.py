from django.urls import include, path  # type: ignore

from . import views

urlpatterns = [
    path("brands/list/", views.BrandListView.as_view(), name="brand_list"),
]
