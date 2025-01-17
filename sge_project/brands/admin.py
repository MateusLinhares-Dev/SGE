from django.contrib import admin

from . import models


@admin.register(models.Brand)
class BrandsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ("name",)
