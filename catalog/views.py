from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def index(request):
    return render(request, 'base.html')


def product_list(request, pk):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/product_list.html', context=context)