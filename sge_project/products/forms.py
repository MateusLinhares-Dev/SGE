from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "title",
            "category",
            "brand",
            "description",
            "serie_number",
            "cost_price",
            "selling_price",
        ]

        widgets = {
            "title": forms.TextInput({"class": "form-control"}),
            "category": forms.Select({"class": "form-control"}),
            "brand": forms.Select({"class": "form-control"}),
            "serie_number": forms.TextInput({"class": "form-control"}),
            "cost_price": forms.NumberInput({"class": "form-control"}),
            "selling_price": forms.NumberInput({"class": "form-control"}),
            "description": forms.Textarea({"class": "form-control", "rows": 3}),
        }
        labels = {
            "title": "Título",
            "category": "Categoria",
            "brand": "Marca",
            "serie_number": "Número de série",
            "cost_price": "Preço de custo",
            "selling_price": "Preço de venda",
            "description": "Descrição",
        }
