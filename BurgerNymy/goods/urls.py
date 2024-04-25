# goods/urls.py

from django.urls import path
from goods import views

app_name = "goods"
urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("burgers/", views.burgers, name='burgers'),
    path("product/", views.product, name="product"),
    path("drinks/", views.drinks, name='drinks'),
    path("product/<slug:product_slug>/", views.product, name="product"),

]
