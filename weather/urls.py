from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.weather_city, name='weathers'),
    path('result/', views.weather_city, name='results')
]
