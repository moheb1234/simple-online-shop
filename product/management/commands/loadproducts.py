import random

from django.core.management import BaseCommand

from product.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = ['sport', 'electronic', 'traveling', 'game', 'digital']
        for name in categories:
            category = Category(name=name)
            category.save()

        product_names = ['Shoe', 'Pants', 'Putin', 'Volleyball ball', 'Football ball', 'Hat', 'Resister', 'Capacitor',
                         'Trans', 'Lamp', 'Towel', 'Suitcase', 'Toy gun', 'CD game', 'Toy ball', 'Monopoly game',
                         'Samsung mobile', 'Apple mobile', 'Power bank', 'Laptop']
        for i in range(len(product_names)):
            all_categories = Category.objects.all()
            price = random.randint(1, 100)
            if 0 < i+1 <= 6:
                product = Product(name=product_names[i], price=price, category=all_categories[0],
                                  image='images/' + str(i + 1) + '.jpg')
                product.save()
            elif 6 < i+1 <= 10:
                product = Product(name=product_names[i], price=price, category=all_categories[1],
                                  image='images/' + str(i + 1) + '.jpg')
                product.save()
            elif 10 < i+1 <= 12:
                product = Product(name=product_names[i], price=price, category=all_categories[2],
                                  image='images/' + str(i + 1) + '.jpg')
                product.save()
            elif 12 < i+1 <= 16:
                product = Product(name=product_names[i], price=price, category=all_categories[3],
                                  image='images/' + str(i + 1) + '.jpg')
                product.save()
            else:
                product = Product(name=product_names[i], price=price, category=all_categories[4],
                                  image='images/' + str(i + 1) + '.jpg')
                product.save()
