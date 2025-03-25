from .views import TaskList
from django.urls import path

urlpatterns = [  # Corrected line
    path('', TaskList.as_view(), name='tasks'),
]