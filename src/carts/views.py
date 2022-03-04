from django.shortcuts import render

from carts.models import Cart
from products.models import Product
from carts.utils import get_or_create_cart
# Create your views here.

def cart(request):
    cart = get_or_create_cart(request)
    return render(request, 'carts/carts.html', {'cart':cart})

def add(request):
    cart = get_or_create_cart(request)
    #print('sfsgsg',request.POST.get('product_id'))
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.products.add(product)
    
    return render(request, 'carts/add.html', {
        'product':product
    })