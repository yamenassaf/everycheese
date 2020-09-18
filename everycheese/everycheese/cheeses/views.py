from django.shortcuts import render
from django.views.generic import ListView
from .models import Cheese
# Create your views here.

class CheeseListView(ListView):
    model = Cheese
    