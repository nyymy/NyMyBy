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
    pass


def cart_remove(request, cart_id):
     cart = Cart.objects.get(id=cart_id)
     cart.delete()

     return redirect(request.META['HTTP_REFERER'])


