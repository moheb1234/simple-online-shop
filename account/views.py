from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, FormView

from account.form import UserRegisterForm, UserLoginForm


class UserRegister(FormView):
    template_name = 'account/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        form.save(form.cleaned_data)
        messages.success(self.request, 'register was done successfully', 'success')
        return super().form_valid(self)


class UserLogin(FormView):
    template_name = 'account/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('product:products')

    def form_valid(self, form):
        try:
            user = form.find_user(form.cleaned_data)
            login(self.request, user)
        except ValueError as ve:
            messages.error(self.request, str(ve), 'danger')
            return redirect(self.request.get_full_path())
        return super().form_valid(self)


class UserLogoutView(LoginRequiredMixin, RedirectView):
    pattern_name = 'account:login'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
