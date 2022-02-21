from django.shortcuts import render
from django.views import generic

from products.models import Product
# Create your views here.

class ProductListView(generic.ListView):
    template_name = 'index,html'
    queryset = Product.objects.all().order_by('title')
    
    def get_context_data(self, **kwars):
        context = super().get_context_data(**kwars)
        context['message'] = 'Listado de productos'
        return context

