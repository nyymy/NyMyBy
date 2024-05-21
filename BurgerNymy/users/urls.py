# burgers/urls.py

from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name='registration'),
    path("profile/", views.profile, name='profile'),
    path("logout/", views.logout, name='logout'),
    path("users_cart/", views.users_cart, name='users_cart'),

    # Add other paths as needed
]

