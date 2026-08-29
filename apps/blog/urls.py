from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Исправленная строка для админки:
    path('admin/', admin.site.urls),

    # Подключение маршрутов вашего приложения из папки apps:
    path('blog/', include('blog.urls')),
]
