from django.urls import path
from . import views

urlpatterns = [
    path('', views.baseview, name='baseview'),
    path('deltask/<int:todo_id>/', views.deltask, name='deletion')
]
