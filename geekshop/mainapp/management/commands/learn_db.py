import json
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import User
from django.db.models import Q

class Command(BaseCommand):
    def handle(self, *args, **options):

        # product = Product.objects.filter(
        #     Q(category__name='Обувь') | Q(id=5)
        # )

        # product = Product.objects.filter(
        #     Q(category__name='Обувь') & Q(id=5)
        # )

        # product = Product.objects.filter(
        #     ~Q(category__name='Обувь')
        # )

        product = Product.objects.filter(
            Q(category__name='Обувь'), id=5
        )