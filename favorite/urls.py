from django.urls import path
from .views import *

app_name = 'favorite'

urlpatterns = [
    path('', FavoriteView.as_view(), name='favorites'),
    path('add/<int:pk>', AddView.as_view(), name='add'),
    path('remove/<int:pk>', RemoveView.as_view(), name='remove'),
]
