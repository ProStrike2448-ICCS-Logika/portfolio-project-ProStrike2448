from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.models import BaseModelForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'custom_auth/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = 'custom_auth:login'


class RegisterView(CreateView):
    template_name = 'custom_auth/register.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form: BaseModelForm):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy('custom_auth:login'))
