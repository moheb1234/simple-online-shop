
from django.views.generic import ListView

from product.filters import ProductFilter
from product.form import  FilterForm
from product.models import Product


class ProductListView(ListView):
    template_name = 'product/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q_param = self.request.GET
        form_initial = {
            'name': q_param.get('name', ''), 'category': q_param.get('category', ''), 'order': q_param.get('order', '')
        }
        filter_form = FilterForm(initial=form_initial)
        context['filter_form'] = filter_form
        return context

    def get_queryset(self):
        return ProductFilter(self.request.GET, queryset=Product.objects.all()).qs
