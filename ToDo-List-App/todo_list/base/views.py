from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task
# Create your views here.



class TaskList(ListView):
# return HttpResponse("To-Do List")
    model = Task
    context_object_name = 'tasks'
