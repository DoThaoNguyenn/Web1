from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.

def show(request):
    data = {'Products': Products.objects.all().order_by('-product_cost')}
    return render(request,'example/products.html',data )

def product_detail(request):
    sp = Products.objects.get(pk=id)
    return render(request, 'example/product_detail.html', {'product':sp})