from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from favorite.models import Favorite


class FavoriteView(LoginRequiredMixin, View):
    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        context = {'favorites': favorites}
        return render(request, 'favorite/favorites.html', context=context)


class AddView(LoginRequiredMixin, View):
    def post(self, request, pk):
        is_exist = not Favorite.objects.get_or_create(user=request.user, product_id=pk)[1]
        if is_exist:
            messages.warning(request, 'this product already exist in your favorites ', 'warning')
            return redirect('product:products')
        messages.success(request, 'product added to your favorites', 'success')
        return redirect('product:products')


class RemoveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        favorite_filter = Favorite.objects.filter(user=request.user, product_id=pk)
        if favorite_filter.exists():
            favorite_filter.delete()
            messages.success(request, 'product removed from your favorites', 'success')
            return redirect('favorite:favorites')
        messages.error(request, 'product not exist', 'danger')
        return redirect('favorite:favorites')
