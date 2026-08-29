from django.urls import path
from django.http import HttpResponse
# Импортируем файл views из текущей папки
from . import views


def home_view(request):
    return HttpResponse("<h1> Главная страница </h1>")


urlpatterns = [
    # Указываем путь к функции через views.имя_функции
    path('', views.home_view, name='home'),
]
