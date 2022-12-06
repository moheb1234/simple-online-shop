from django.core.management import BaseCommand

from product.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Product.objects.first():
            self.stdout.write('There are no products in the database')
        else:
            Category.objects.all().delete()
            Product.objects.all().delete()
            self.stdout.write('all products are removed')
