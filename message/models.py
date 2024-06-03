from datetime import datetime

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст рассылки')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.email}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Send(models.Model):
    STATUS_CHOICE = [('created', 'создана'),
                     ('started', 'запущена'),
                     ('finished', 'закончена')]
    PERIODICITY_CHOICE = [('daily', 'каждый день'),
                          ('weekly', 'каждую неделю'),
                          ('monthly', 'каждый месяц')]
    date_and_time_of_first_send = models.DateTimeField(default=datetime.now)
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICE, default='daily')
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='created')
    client = models.ManyToManyField(Client, related_name='mailings')
    message = models.OneToOneField(Message, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f'Рассылка {self.id} - {self.status}'
