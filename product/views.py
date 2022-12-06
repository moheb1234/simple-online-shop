from django.shortcuts import render
from django.views import View

from product.form import CategoryFilterForm, SearchFilterForm
from product.models import Product


class Products(View):
    def get(self, request, name=None):
        if name:
            products = Product.order_by(name)
        else:
            products = Product.objects.all()
        category_form = CategoryFilterForm()
        search_form = SearchFilterForm()
        if 'category' in request.GET:
            category = request.GET['category']
            if category != '':
                products = products.filter(category__id=category)
            category_form = CategoryFilterForm(initial={'category': category})
        if 'name' in request.GET:
            name = request.GET['name']
            if name != '':
                products = products.filter(name__startswith=name)
            search_form = SearchFilterForm(initial={'name': name})
        return render(request, 'product/products.html'
                      , {'products': products, 'category_form': category_form, 'search_form': search_form})
