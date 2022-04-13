from django.contrib import admin
from mainapp.models import Product, ProductCategory

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Product)

# @admin.register(Product)
# class Product(admin.ModelAdmin):
#     list_display = ('name', 'price', 'quantity', 'category')
#     fields = ('name', 'image', 'descriptions', ('price', 'quantity'), 'category')
#     readonly_fields = ('descriptions', )
#     ordering = ('name', 'price')
#     search_fields = ('name', )