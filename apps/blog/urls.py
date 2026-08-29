from django.urls import path
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<h1> Главная страница </h1>")


urlpatterns = [
    # Только одна строка для главной страницы!
    path('', home_view, name='home'),
]
