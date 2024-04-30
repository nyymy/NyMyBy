from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from django.http import Http404

from goods.models import Products
from goods.utils import q_search


# Create your views here.
def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    if not goods.exists():
        raise Http404("No products found for the given category.")

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Home - categories",
        "goods": current_page,
        "slug_url": category_slug
    }

    return render(request, "catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, "product.html", context=context)
