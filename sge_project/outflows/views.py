from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from . import forms
from rest_framework import generics
from . import serializers
from django.urls import reverse_lazy
from . import models
from app.metrics import get_sales_metrics


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outflow
    template_name = "Outflow_list.html"
    context_object_name = "outflows"
    paginate_by = 10
    permission_required = "outflows.view_outflow"

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sales_metrics"] = get_sales_metrics()

        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outflow
    template_name = "Outflow_create.html"
    form_class = forms.OutflowForm
    success_url = reverse_lazy("outflow_list")
    permission_required = "outflows.add_outflow"


class OutflowDetailView(DetailView, PermissionRequiredMixin):
    model = models.Outflow
    template_name = "Outflow_detail.html"
    permission_required = "outflows.view_outflow"


class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer


class OutflowRetrieveUpdateDestroyView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer
