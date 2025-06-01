from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # <- change views.home to views.index
]
