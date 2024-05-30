from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .utils import get_user_carts

from carts.models import Cart
from goods.models import Products
# Create your views here.


def cart_add(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = Products.objects.get(id=product_id)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)

            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)

        else:
            carts = Cart.objects.filter(
                session_key=request.session.session_key, product=product)

            if carts.exists():
                cart = carts.first()

                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

        user_cart = get_user_carts(request)

        cart_items_html = render_to_string(
            "carts/includes/included_cart.html", {'carts': user_cart}, request=request)

        response_data = {
            'message': 'Added to cart',
            'cart_items_html': cart_items_html,
        }

        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)



def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {'carts': cart}, request=request)

    response_data = {
        "message": "Quantity changed",
        "cart_items_html": cart_items_html,
        "quantity": quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):

    cart_id = request.POST.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
         "carts/includes/included_cart.html", {'carts': user_cart}, request=request)

    response_data = {
        "message": "Product removed",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)


