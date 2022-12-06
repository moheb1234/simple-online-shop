from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)

    @staticmethod
    def order_by(name):
        products = Product.objects.all()
        if name == 'Newest':
            products = products.order_by('created_date__date')
        elif name == 'Oldest':
            products = products.order_by('-created_date')
        elif name == 'Expensive':
            products = products.order_by('-price')
        elif name == 'Cheapest':
            products = products.order_by('price')
        return products
