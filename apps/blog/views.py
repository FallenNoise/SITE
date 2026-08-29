from django.shortcuts import render
from django.http import HttpResponse

# Переносим функцию сюда
def home_view(request):
    return HttpResponse("Главная страница из файла views.py")