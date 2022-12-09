from django.db import models


class CartManager(models.Manager):
    def add(self, user, product):
        cart = self.filter(user=user, product=product).first()
        if cart:
            cart.quantity += 1
            cart.save()
        else:
            self.create(user=user, product=product)

    def total_price(self, user):
        user_cart = self.filter(user=user)
        total_price = 0
        for cart in user_cart:
            total_price += cart.total_price()
        return total_price
