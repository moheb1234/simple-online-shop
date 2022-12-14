from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
