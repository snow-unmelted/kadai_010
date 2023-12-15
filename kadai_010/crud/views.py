from django.shortcuts import render
from django.views.generic import TemplateView, ListView 
from django.views.generic.edit import DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    paginate = 3

class ProductDetailView(DetailView):
    model = Product

