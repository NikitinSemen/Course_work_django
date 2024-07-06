from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from message.forms import MessageForm, ClientForm
from message.models import Message, Client, Send


class BaseView(TemplateView):
    template_name = '/home/webcam/course_work_django/message/templates/message/base.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Message, Client, form=ClientForm, extra=2)
        context_data['formset'] = SubjectFormset
        return context_data


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'text')

    def get_success_url(self):
        return


class SendListView(ListView):
    model = Send
