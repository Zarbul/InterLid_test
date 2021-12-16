from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from .forms import ManagerCreationForm
from .models import Manager

User = get_user_model()


class Login(LoginView):
    template_name = 'users/login.html'


class Register(generic.CreateView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class Logout(LogoutView):
    next_page = '/'
