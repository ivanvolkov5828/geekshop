from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request, id_category=None, page=1):

    if id_category:
        # products = Product.objects.filter(category_id=id_category)
	products = Product.objects.filter(category_id=id_category).select_related()
    else:
        # products = Product.objects.all()
	products = Product.objects.all().select_related()

    pagination = Paginator(products, per_page=3)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)

    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': product_pagination
        # 'products': Product.objects.filter(category_id=id_category) if id_category else Product.objects.all()
    }

    return render(request, 'mainapp/products.html', content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'
