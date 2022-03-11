from django.shortcuts import get_object_or_404
from django.shortcuts import redirect,render
from carts.models import Cart
from products.models import Product
from carts.utils import get_or_create_cart
from carts.models import CartProducts

# Create your views here.

def cart(request):
    cart = get_or_create_cart(request)
    return render(request, 'carts/carts.html',{'cart':cart})

def add(request):
    cart = get_or_create_cart(request)
    #product = Product.objects.get(pk=request.POST.get('product_id'))
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))
    cart_product = CartProducts.objects.create_or_update_quantity(
         cart=cart,
         product=product,
         quantity=quantity,
    )
    
    return render(request, 'carts/add.html',{
        'quantity':quantity,
        'cart_product':cart_product,
        'product':product,
    })
    
def remove(request):
    cart = get_or_create_cart(request)
    prod = get_object_or_404(Product, pk=request.POST.get('product_id'))
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.products.remove(product)
    return redirect('carts:cart')
    