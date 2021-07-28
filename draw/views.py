# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def theme(request):
    return render(request, 'draw/theme.html')

def animals(request):
    return render(request, 'draw/animals.html')

def random(request):
    return render(request, 'draw/random.html')

def structures(request):
    return render(request, 'draw/structures.html')

def result(request):
    return render(request, 'draw/result.html')
