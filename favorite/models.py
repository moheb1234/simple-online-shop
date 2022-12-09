from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-add_date',)
