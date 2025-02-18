from django.contrib import admin

from . import models


@admin.register(models.Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = (
        "supplier",
        "product",
        "quantity",
        "created_at",
        "update_at",
    )
    search_fields = ("supplier__name", "product__title")
