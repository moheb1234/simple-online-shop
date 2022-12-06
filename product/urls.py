from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', Products.as_view(), name='products'),
    path('order/<str:name>', Products.as_view(), name='order_filter'),
]
