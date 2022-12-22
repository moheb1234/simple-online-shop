from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
]
