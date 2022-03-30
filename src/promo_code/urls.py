from django.urls import path

from promo_code import views

app_name = 'promo_code'

urlpatterns = [
    path('valida', views.validate, name='validar'),
]
