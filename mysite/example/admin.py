from django.contrib import admin

from .models import Product_catogories, Products
# Register your models here.

admin.site.register(Product_catogories)
# admin.site.register(Products)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_cost']
    list_filter =   ['product_cost']
    search_fields = ['product_name']
admin.site.register(Products,ProductsAdmin)