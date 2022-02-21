from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from StoreOnline.forms import RegisterForm
from django.contrib.auth.models import User
from products.models import Product


def index(request):
    product = Product.objects.all().order_by('-title')
    context={
        
            'title': 'Productos',
            'message': 'Listado de productos',
            'products': product,
    }
    return render(request, "index.html", context)

def login_view(request):
    if request.user.is_authenticate:
        return redirect('index')
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
    if request.user.is_authenticate:
        return redirect('index')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        
        if user:
            login(request, user)
            messages.success(request, 'El usuario ha sido creado correctamente')
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
