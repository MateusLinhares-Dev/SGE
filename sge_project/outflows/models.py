from django.db import models
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product, models.PROTECT, related_name="outflows")
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)  # altera a data quando editado

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(self.product)
