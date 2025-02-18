from django.urls import path  # type: ignore

from . import views

urlpatterns = [
    path("inflows/list/", views.InflowListView.as_view(), name="inflow_list"),
    path(
        "inflows/create/",
        views.InflowCreateView.as_view(),
        name="inflow_create",
    ),
    path(
        "inflows/<int:pk>/detail/",
        views.InflowDetailView.as_view(),
        name="inflow_detail",
    ),
    path(
        "inflows/<int:pk>/detail/",
        views.InflowDetailView.as_view(),
        name="inflow_detail",
    ),
    path(
        "api/v1/inflows",
        views.InflowCreateListAPIView.as_view(),
        name="inflows-create-list-api-view",
    ),
    path(
        "api/v1/inflows/<int:pk>",
        views.InflowRetrieveUpdateDestroyView.as_view(),
        name="inflows-detail-api-view",
    ),
]
