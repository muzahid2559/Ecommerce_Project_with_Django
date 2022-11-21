# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# Import views
from django.views.generic import DetailView, ListView

# Models
from App_Shop.models import Product


# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

