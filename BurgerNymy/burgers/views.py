from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.

def menu(request):
    return render(request, "menu.html")


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")