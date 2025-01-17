from brands.models import Brand
from categories.models import Category
from django.db import models  # type: ignore


class Product(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(
        max_digits=20, decimal_places=2
    )  # Usar para formatação de dinheiro - decimal
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)  # altera a data quando editado

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
