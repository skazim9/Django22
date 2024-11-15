from django.shortcuts import render, get_object_or_404
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


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context=context)