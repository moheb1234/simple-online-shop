from django.contrib.auth.models import User
from django.db import models

from cart.manager import CartManager
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    modify = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    class Meta:
        ordering = ('-create_date',)

    def total_price(self):
        return self.quantity * self.product.price
