from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Cheese

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese
    
    fields=['name','description','firmness',"country_of_origin",'creator']

class CheeseCreateView(LoginRequiredMixin,CreateView):
    model = Cheese
    fields = ['name','description','firmness','country_of_origin',]
    
    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


