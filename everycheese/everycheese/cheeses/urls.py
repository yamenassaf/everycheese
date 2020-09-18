from django.urls import path
from .views import CheeseListView

app_name = "cheeses"
urlpatterns = [
    path('',CheeseListView.as_view(),name='list')
]