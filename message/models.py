from datetime import datetime

from django.db import models
from django.utils import timezone

from users.models import User

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
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')

    def __str__(self):
        return f'{self.name}'

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
    date_and_time_of_first_send = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICE, default='daily',
                                   verbose_name='Частота отправки')
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='created', verbose_name='статус рассылки')
    client = models.ManyToManyField(Client, related_name='mailings', verbose_name='Адрессаты')
    message = models.OneToOneField(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f'Рассылка {self.id}'


class MailingLog(models.Model):
    send = models.ForeignKey(Send, on_delete=models.CASCADE, verbose_name='логгируемая рассылка',
                             help_text='логгируемая рассылка', related_name='mailing_logs')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    status = models.BooleanField(verbose_name='статус попытки')
    mail_answer = models.TextField(verbose_name='ответ почтового сервера')

    def __str__(self):
        return f'Рассылка {self.created_at}'
