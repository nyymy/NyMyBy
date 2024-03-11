from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.

def specials(request):
    return render(request, "specials.html")




def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")
