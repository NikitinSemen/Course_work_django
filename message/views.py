from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from message.models import Message


class BaseView(TemplateView):
    template_name = '/home/webcam/course_work_django/message/templates/message/base.html'


class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'text')
    # success_url = reverse_lazy()


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'text')

    def get_success_url(self):
        return
