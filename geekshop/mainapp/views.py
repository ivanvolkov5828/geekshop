from django.shortcuts import render
# подключили наши модельки(таблицы в б.д), чтобы добавить их в контроллеры
from mainapp.models import Product, ProductCategory


#Create your views here.
def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request,'mainapp/index.html',content)


def products(request):
    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all()
        }

    return render(request, 'mainapp/products.html', content)

