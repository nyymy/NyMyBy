from django.shortcuts import render
from goods.models import Products


# Create your views here.
def catalog(request):
    goods = Products.objects.all()

    context = {
        "title": "Home - categories",
        "goods": goods,
    }
    return render(request, "catalog.html", context)


def drinks(request):
    context = {
        "title": "Drinks",
        "goods": [
            {
                "image": "https://cdn.pixabay.com/photo/2014/09/12/18/20/can-443123_1280.png",
                "name": "Cola",
                "description": "Cold cola",
                "price": 2.5,
            },
            {
                "image": "https://cdn.pixabay.com/photo/2019/04/14/15/37/bottledwater-4127009_1280.png",
                "name": "Water",
                "description": "Nice water",
                "price": 1.4,
            },
        ]
    }

    return render(request, "drinks.html", context)


def burgers(request):
    context = {
        "title": "Burgers",
        "goods": [
            {
                "image": "https://static01.nyt.com/images/2023/07/13/multimedia/13xp-cheese-king/13xp-cheese-king-superJumbo.jpg",
                "name": "Cheesburger",
                "description": "A classic burger with a juicy beef patty and melted cheese.",
                "price": 5,
            },
            {
                "image": "https://i.pinimg.com/564x/cc/9a/7f/cc9a7f913081588ba2a16974c91728a0.jpg",
                "name": "Hamburger",
                "description": "Grilled chicken breast topped with fresh lettuce and mayo.",
                "price": 7.1,
            },
            {
                "image": "https://i.pinimg.com/564x/5b/f8/ca/5bf8ca02fc499db71f4b34d86813edf0.jpg",
                "name": "Veggie Burger",
                "description": "Perfect for vegetarians, a tasty patty made from fresh vegetables.",
                "price": 6.4,
            },
        ]
    }
    return render(request, "burgers.html", context)


def product(request):
    return render(request, )
