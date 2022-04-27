from django.shortcuts import render, redirect
from .models import Product

def product(request):
    context = {
        'product' : Product.objects.all()
    }
    return render(request, 'product.html', context)

# Create your views here.
