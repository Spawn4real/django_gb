import random

from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import ProductCategory, Product

main_menu = [
    {'href': '/', 'name': 'Домой'},
    {'href': 'products', 'name': 'Продукты'},
    {'href': 'contact', 'name': 'Контакты'},
]


def main(request):
    title = 'Главная'
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'main_menu': main_menu,
        'products': products
    }
    return render(request, 'mainapp/index.html', context=context, )


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_products():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)

    return same_products


def products(request, pk=None, page=1):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
    hot_products = get_hot_products()
    same_products = get_same_products(hot_products)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'pk': 0, 'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 1)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'main_menu': main_menu,
            'category': category,
            'products': products_paginator,
            'hot_products': hot_products,
            'same_products': same_products,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context=context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'main_menu': main_menu,
        'hot_products': hot_products,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'main_menu': main_menu,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title,
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/contact.html', context=context)
