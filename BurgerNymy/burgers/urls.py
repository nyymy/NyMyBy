# burgers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("menu/", views.menu, name='menu'),
    path("about/", views.about, name='about'),
    # Add other paths as needed
]
