from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from StoreOnline.forms import RegisterForm


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
        #print("sfdssssssssssssssssssssssssssssssssssssssss",username)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o Contraseña incorrectos')
        
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada correctamente')
    return redirect('login')

def register(request):
    form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
