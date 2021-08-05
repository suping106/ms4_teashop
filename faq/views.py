from django.shortcuts import render
from .models import FAQ
from products.models import Product
# Create your views here.


def faq(request):
    """    A view to return the FAQ page    """

    faq = FAQ.objects.all()
    # products = Product.objects.all()

    # if request.GET:
    #     if 'product' in request.GET:
    #         all_products = Product.objects.all()
    #         product = request.GET['product']
    #         products = all_products.filter(name=product)

    context = {
        'faq': faq
        # 'products': products
    }

    return render(request, 'faq/faq.html', context)
