from django.contrib import admin
from django.urls import path
from django.urls import include
from api import views

urlpatterns = [
    path('index/', views.index),
]