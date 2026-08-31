from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Переносим функцию сюда


def home_view(request):
    return HttpResponse("Главная страница из файла views.py")


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})
