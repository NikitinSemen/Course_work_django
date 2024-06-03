from django.urls import path

from message.apps import MessageConfig
from message.views import BaseView, MessageCreateView, MessageListView

app_name = MessageConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('message/create', MessageCreateView.as_view(), name='message_create')
]
