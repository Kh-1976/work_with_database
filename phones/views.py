from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def sort_func(request):
    sorting = request.GET.get('sort', '')
    if sorting == 'name':
        return Phone.objects.order_by('name')
    elif sorting == 'min_price':
        return Phone.objects.order_by('price')
    elif sorting == 'max_price':
        return Phone.objects.order_by('-price')
    else:
        return Phone.objects.all()


def show_catalog(request):
    phone = sort_func(request)
    template = 'catalog.html'
    context = {
        'phones': phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).get()
    context = {
        'phone': phone
    }
    return render(request, template, context)
