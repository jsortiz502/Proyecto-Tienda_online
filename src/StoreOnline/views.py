from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'title':'Productos',
        'message':'Listado de productos',
        'products':[
            {'title':"Playera", 'precio':25000, 'stock':True},
            {'title':"Gafas", 'precio':35000, 'stock':True},
            {'title':"Short", 'precio':30000, 'stock':False},
        ]
    }
    return render(request, "index.html", context)

