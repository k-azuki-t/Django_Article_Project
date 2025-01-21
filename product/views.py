from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ProductTopView(TemplateView):
    template_name = 'product/product_top.html'