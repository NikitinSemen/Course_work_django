from django.contrib import admin

from message.models import Client, Message, Send, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    list_filter = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = (Client, Message, 'periodicity', 'date_and_time_of_first_send', 'status')


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = (Send, 'created_at', 'status', 'mail_answer')