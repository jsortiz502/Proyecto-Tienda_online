from django.shortcuts import render
from django.views import generic
from shipping_address.models import ShippingAddress
from shipping_address.forms import ShippingAddressForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404




@login_required(login_url='login')
#cuando un def esta fuera de la clase es una funcion y por olbigacion debe llevar el request
def create(request):
    form = ShippingAddressForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not request.user.has_shipping_address()
        shipping_address.save()
        messages.success(request, 'Direccion Creada con Exito')
        return redirect('shipping_address:shipping_address')
    return render(request, 'create.html', {'form':form})
    
@login_required(login_url='login')
def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)
    if request.user.id != shipping_addres.user_id:
        return redirect('carts:cart')
    if request.user.has_shipping_address():
        request.user.shipping_address.update_default()
    shipping_address.update_default(True)
    
    return redirect('shipping_address:shipping_address')
class ShippingAddressListView(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    model = ShippingAddress
    template_name = 'shipping_addresses.html'
    
    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')
    
class ShippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    login_url = 'login'
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'update.html'
    success_message = 'Direccion Actualizada Exitosamente'
    
    def get_success_url(self):
        return reverse('shipping_address:shipping_address')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')
        
        return super(ShippingAddressUpdateView, self).dispatch(request, *args, **kwargs)
            
class ShippingAddressDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = 'login'
    models = ShippingAddress
    template_name = 'delete.html'
    succes_url = reverse_lazy('shipping_address:shipping_address')
    
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().default:
            return redirect('shipping_address:shipping_address')
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart')
        return super(ShippingAddressDeleteView, self).dispatch(request, *args, **kwargs)
