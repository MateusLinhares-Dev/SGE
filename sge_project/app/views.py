from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from .metrics import (
    get_product_metrics,
    get_sales_metrics,
    get_daily_sales_data,
    get_daily_sales_quantity_data,
    get_product_count_by_category,
    get_product_count_by_brand,
)


@login_required(login_url="login")
def home(request):

    product_metrics = get_product_metrics()
    sales_metrics = get_sales_metrics()
    daily_sales_data = get_daily_sales_data()
    daily_sales_quantity_data = get_daily_sales_quantity_data()
    product_count_by_category = get_product_count_by_category()
    product_count_by_brand = get_product_count_by_brand()

    context = {
        "product_metrics": product_metrics,
        "sales_metrics": sales_metrics,
        "daily_sales_data": json.dumps(daily_sales_data),
        "daily_sales_quantity_data": json.dumps(daily_sales_quantity_data),
        "product_count_by_category": json.dumps(product_count_by_category),
        "product_count_by_brand": json.dumps(product_count_by_brand),
    }

    return render(request, "home.html", context)
