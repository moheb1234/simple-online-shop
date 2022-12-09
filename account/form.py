import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cd = super().clean()
        password = cd.get('password')
        confirm_password = cd.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('password not match')

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 8:
            raise ValidationError('password length must be at least 8 character')
        if not re.search('\\d', data):
            raise ValidationError('password must contains at least one digits')
        if re.search('\\s', data):
            raise ValidationError('password must not contains any space')
        if re.search('[a-zA-z]', data):
            raise ValidationError('password must contains at least one letter')
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) < 3:
            raise ValidationError('username is too short')
        if re.search('\\s', data):
            raise ValidationError('username must not contains any space')
        if User.objects.filter(username=data).first():
            raise ValidationError('this username already taken')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).first():
            raise ValidationError('this email already taken')
        return data

    def save(self, clean_data: dict):
        x = clean_data
        print(x)
        first_name = clean_data['first_name']
        last_name = clean_data['last_name']
        username = clean_data['username']
        email = clean_data['email']
        password = clean_data['password']
        user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.save()


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def find_user(self, clean_data: dict):
        username = clean_data['username_or_email']
        password = clean_data['password']
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if not user:
            raise ValueError('user not founded')
        if not user.check_password(password):
            raise ValueError('password is wrong')
        return user
