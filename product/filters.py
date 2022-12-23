import django_filters
from django.db.models import QuerySet, Count
from django_filters import filters, OrderingFilter


class ProductFilter(django_filters.FilterSet):
    name = filters.CharFilter(lookup_expr='istartswith')
    category = filters.CharFilter()
    order = filters.CharFilter(method='ordering')
    available = filters.CharFilter(method='check_availability')

    def ordering(self, queryset, name, value):
        return queryset.order_by(value)

    def check_availability(self, queryset, name, value):
        if value:
            return queryset.filter(is_available=True)
        return queryset
