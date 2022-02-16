from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print('Usted esta auntenticado')
        else:
            print('Es hacker')
        
    return render(request, 'users/login.html',{})

