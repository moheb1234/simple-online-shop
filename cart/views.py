from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from cart.models import Cart
from product.models import Product


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        return render(request, 'cart/cart.html',
                      {'cart_items': cart_items, 'total_price': Cart.objects.total_price(request.user)})


class AddView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        if product:
            if product.is_available:
                Cart.objects.add(request.user, product)
                messages.success(request, 'product added successfully', 'success')
                return redirect('product:products')
            messages.warning(request, 'product is not available', 'danger')
            return redirect('product:products')
        messages.error(request, 'no product founded', 'danger')
        return redirect('product:products')


class RemoveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        cart = Cart.objects.filter(product_id=pk, user=request.user).first()
        if cart:
            cart.delete()
            messages.success(request, 'product successfully removed', 'success')
            return redirect('cart:cart')
        messages.error(request, 'this product is not in your cart', 'danger')
        return redirect('cart:cart')
