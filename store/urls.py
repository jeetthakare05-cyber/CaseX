from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("product/<int:product_id>/",
         views.product_detail,
         name="product_detail"),

    path(
    "add-to-cart/<int:product_id>/",
    views.add_to_cart,
    name="add_to_cart",
),
    path(
    "cart/",
    views.cart,
    name="cart",
),
    path(
    "remove-from-cart/<int:cart_id>/",
    views.remove_from_cart,
    name="remove_from_cart",
),
    path(
    "increase/<int:cart_id>/",
    views.increase_quantity,
    name="increase_quantity",
),

    path(
    "decrease/<int:cart_id>/",
    views.decrease_quantity,
    name="decrease_quantity",
),

    path("checkout/",views.checkout,name="checkout",),

    path("place-order/", views.place_order, name="place_order"),

    path("my-orders/",views.my_orders,name="my_orders",),

    path("review/<int:product_id>/",views.add_review,name="add_review",),

    path(
    "wishlist/",
    views.wishlist,
    name="wishlist",),

    path(
    "wishlist/add/<int:product_id>/",
    views.add_to_wishlist,
    name="add_to_wishlist",),

    path(
    "wishlist/remove/<int:wishlist_id>/",
    views.remove_from_wishlist,
    name="remove_from_wishlist",),

    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("suggestions/", views.suggestions, name="suggestions"),
]
