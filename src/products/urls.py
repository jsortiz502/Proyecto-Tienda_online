from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='prodcut'),
]