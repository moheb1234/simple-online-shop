import django_filters
from django.db.models import QuerySet
from django_filters import filters, OrderingFilter


class ProductFilter(django_filters.FilterSet):
    name = filters.CharFilter(lookup_expr='istartswith')
    category = filters.CharFilter()
    order = filters.CharFilter(method='ordering')

    def ordering(self, queryset, name, value):
        return queryset.order_by(value)
