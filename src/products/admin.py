from django.contrib import admin
from products.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'price', 'image')
    list_display = ('__str__', 'slug', 'create_at')

admin.site.register(Product, ProductAdmin)

