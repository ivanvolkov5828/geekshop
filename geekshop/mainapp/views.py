from datetime import datetime
from django.shortcuts import render

# подключили наши модельки(таблицы в б.д), чтобы добавить их в контроллеры
from mainapp.models import Product, ProductCategory

# Create your views here.


def index(request):
    content = {
        # титл страницы
        'title': 'geekshop',
        # заголовок
        'header': 'GeekShop Store',
        # описание
        'description': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        # кнопка
        'button': 'Начать покупки',
        # каталог
        'catalog': 'Каталог',
        # войти
        'enter': 'Войти',
        # пользователь
        'user': 'User',
        # выйти
        'go_out': 'Выйти',
        # дата
        'date': datetime.now()
    }

    return render(request, 'mainapp/index.html', content)


def products(request):
    # соответственно нам надо передать в переменную данные из таблицы
    categories = ProductCategory.objects.all()
    # тянем из базы для карточек товаров
    cards = Product.objects.all()

    content = {
        # титл страницы products
        'title': 'GeekShop - Каталог',
        # категории товаров
        'categories': categories,
        # карточки товаров
        'cards': cards,
        # предыдущие товары
        'previous': 'Previous',
        # страницы
        'pages': [1, 2, 3],
        # следующая страница
        'next': 'Next'
    }

    return render(request, 'mainapp/products.html', content)
