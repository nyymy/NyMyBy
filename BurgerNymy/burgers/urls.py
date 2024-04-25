# burgers/urls.py

from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name='about'),
    path("specials/", views.specials, name='specials'),
    # Add other paths as needed
]

