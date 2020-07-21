from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='mycarthome'),
    path('search/', views.search, name='cartsearch'),
]
