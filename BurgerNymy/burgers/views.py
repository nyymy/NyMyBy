from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from goods.models import Categories


# Create your views here.


def specials(request):
    return render(request, "specials.html")


def home(request):

    context = {
        'title': 'Home Page'
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")
