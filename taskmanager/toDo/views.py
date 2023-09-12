from django.shortcuts import render
from django.http import HttpResponse


def setTask(request):
    return render(request, 'toDo/index.html')


def getTask(request):
    return render(request, 'toDo/getTasker.html')
