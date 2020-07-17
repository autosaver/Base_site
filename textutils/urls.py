from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.text_input, name='textutils_input'),
    path('result/', views.text_process, name='textutils_process'),
]
