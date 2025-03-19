from . import views
from django.urls import path

urlpatterns = [  # Corrected line
    path('', views.todo_list, name='todo_list'),
]