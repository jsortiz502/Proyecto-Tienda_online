from django.urls import path

from shipping_address import views

app_name = 'shipping_addresses'


urlpatterns = [
    path('',views.ShippingAddressListView.as_view(), name='shipping_addresses')
]
