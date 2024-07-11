from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Заголовок', help_text="Введите заголовок"
    )
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    author = models.ForeignKey(User, verbose_name='автор', on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name='Текст поста', help_text='Введите содержимое поста')
    photo = models.ImageField(upload_to="blog/", verbose_name='фото', help_text='Вставьте фото', **NULLABLE)
    created_at = models.DateField(**NULLABLE, auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик просмотров'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

