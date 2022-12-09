from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:pk>', AddView.as_view(), name='add'),
    path('remove/<int:pk>', RemoveView.as_view(), name='remove'),
]
