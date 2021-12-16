from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'products': Product.objects.all()[:4],
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    return render(request, 'mainapp/contact.html')


def products(request, pk=None):
    context = {
        'links_menu': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context=context)
