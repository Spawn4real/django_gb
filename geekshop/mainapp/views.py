from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
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


def products(request, pk=None):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'main_menu': main_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'main_menu': main_menu,
        'products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    title = 'Контакты'
    context = {
        'title': title,
        'main_menu': main_menu,
    }
    return render(request, 'mainapp/contact.html', context=context)
