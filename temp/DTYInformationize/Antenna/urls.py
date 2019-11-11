from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.show_index),
]