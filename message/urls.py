from django.urls import path

from message.apps import MessageConfig
from message.views import BaseView, MessageCreateView, MessageListView, SendListView, MessageUpdateView, SendDetailView, \
    SendCreateView, SendUpdateView

app_name = MessageConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('send/', SendListView.as_view(), name='send_list'),
    path('send/<int:pk>/', SendDetailView.as_view(), name='send_detail'),
    path('send/create/<int:pk>/', SendCreateView.as_view(), name='send_create'),
    path('send/<int:pk>/update/', SendUpdateView.as_view(), name='send_update'),
]
