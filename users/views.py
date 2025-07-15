from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import UserRegisterForm

class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy('login')