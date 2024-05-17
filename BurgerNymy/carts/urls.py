# goods/urls.py

from django.urls import path
from carts import views

app_name = "carts"
urlpatterns = [
    path("card_add/<int:product_id>", views.cart_add, name="cart_add"),
    path("card_change/<int:product_id>", views.cart_change, name="cart_change"),
    path("card_remove/<int:product_id>", views.cart_remove, name="cart_remove"),

]
