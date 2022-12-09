from urllib.request import Request

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from account.form import UserRegisterForm, UserLoginForm


class UserRegister(View):
    form_class = UserRegisterForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save(form.cleaned_data)
            messages.success(request, 'register was done successfully', 'success')
            return redirect('account:login')
        return render(request, self.template_name, {'form': form})


class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            try:
                user = form.find_user(form.cleaned_data)
                login(request, user)
            except ValueError as ve:
                messages.error(request, str(ve), 'danger')
                return redirect('account:login')
            return redirect('product:products')
        return render(request, self.template_name, {'form': form})


class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('account:login')
        return redirect('account:login')
