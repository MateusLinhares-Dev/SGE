from django.contrib import admin

from . import models


@admin.register(models.Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "created_at", "update_at")
    search_fields = ("product__title",)
