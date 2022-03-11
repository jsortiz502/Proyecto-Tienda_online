from django.urls import path

from carts import views

app_name = 'orders'

urlpatterns = [
    path('',views.order, name='orders'),
]