from datetime import datetime
from django.shortcuts import render

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
    content = {
        # титл страницы products
        'title': 'GeekShop - Каталог',
        # категории товаров
        'categories': [
            {'name': 'Новинки'},
            {'name': 'Одежда'},
            {'name': 'Обувь'},
            {'name': 'Аксессуары'},
            {'name': 'Подарки'},
        ],
        # карточки товаров
        'cards': [
            {
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'basket': 'Отправить в корзину',
             'link': 'vendor/img/products/Adidas-hoodie.png'
            },
            {
              'name': 'Синяя куртка The North Face',
              'price': '23 725,00 руб.',
              'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
              'basket': 'Отправить в корзину',
              'link': 'vendor/img/products/Blue-jacket-The-North-Face.png'
            },
            {
              'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
              'price': '3 390,00 руб.',
              'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
              'basket': 'Отправить в корзину',
              'link': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
            },
            {
              'name': 'Черный рюкзак Nike Heritage',
              'price': '2 340,00 руб.',
              'description': 'Плотная ткань. Легкий материал.',
              'basket': 'Отправить в корзину',
              'link': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
            },
            {
              'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
              'price': '13 590,00 руб.',
              'description': 'Гладкий кожаный верх. Натуральный материал.',
              'basket': 'Отправить в корзину',
              'link': 'vendor/img/products/Black-Dr-Martens-shoes.png'
            },
            {
              'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
              'price': '2 890,00 руб.',
              'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
              'basket': 'Отправить в корзину',
              'link': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
            }
        ],
        'previous': 'Previous',
        # страницы
        'pages': [1, 2, 3],
        # следующая страница
        'next': 'Next'
    }

    return render(request, 'mainapp/products.html', content)
