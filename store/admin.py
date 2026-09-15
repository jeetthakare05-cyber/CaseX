from django.contrib import admin
from .models import Product, Cart, Order ,Review, Wishlist
from .models import Suggestion

# Register your models here.
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Suggestion)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "price",
        "stock",
        "is_available",
    )

    search_fields = (
        "name",
        "brand",
    )

    list_filter = (
        "brand",
        "is_available",
    )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
        "quantity",
        "added_at",
    )

    search_fields = (
        "user__username",
        "product__name",
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer_name",
        "customer_email",
        "total_price",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "customer_email",
    )