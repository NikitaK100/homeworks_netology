from phones.models import Phone
from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    get_type_sort = request.GET.get('sort')
    
    if get_type_sort == 'name':
        phones_sort_by_name = Phone.objects.order_by('name')
        context = {'phones': phones_sort_by_name}

    elif get_type_sort == 'min_price':
        phones_sort_min_price = Phone.objects.order_by('price')
        context = {'phones': phones_sort_min_price}
    
    elif get_type_sort == 'max_price':
        phones_sort_min_price = Phone.objects.order_by('-price')
        context = {'phones': phones_sort_min_price}

    else:
        phones = Phone.objects.all()
        context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
