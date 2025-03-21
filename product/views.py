from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

class ProductTopView(ListView):
    template_name = 'product/product_top.html'
    model = Product