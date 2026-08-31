from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст поста')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title
