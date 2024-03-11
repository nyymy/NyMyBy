# goods/urls.py

from django.urls import path
from goods import views

app_name = "goods"
urlpatterns = [
    path("", views.catalog, name="index"),
    path("burgers/", views.burgers, name='burgers'),
    path("product/", views.product, name="product"),
    path("drinks/", views.drinks, name='drinks'),
]
