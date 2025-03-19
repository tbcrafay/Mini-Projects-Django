from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def todo_list(request):
    return HttpResponse("To-Do List") # Or your template rendering logic.