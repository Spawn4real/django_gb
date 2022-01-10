from django.shortcuts import render

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
    return render(request, 'mainapp/index.html', context=context,)


def products(request):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    # links_menu = [
    #     {'href': 'products_all', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]
    context = {
        'title': title,
        'links_menu': links_menu,
        'main_menu': main_menu,
        'products': products
    }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title,
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/contact.html', context=context)

