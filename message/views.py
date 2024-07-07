from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView

from message.forms import MessageForm, ClientForm, SendForm
from message.models import Message, Client, Send


class BaseView(TemplateView):
    template_name = '/home/webcam/course_work_django/message/templates/message/base.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('message:message_update', kwargs={'pk': instance.pk}))


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'text')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Message, Client, form=ClientForm, extra=2)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('message:send_create', kwargs={'pk': self.object.pk})


class SendListView(ListView):
    model = Send


class SendDetailView(DetailView):
    model = Send


from django.core.mail import send_mail


class SendCreateView(CreateView):
    model = Send
    form_class = SendForm

    def get_form_kwargs(self):
        kwargs = super(SendCreateView, self).get_form_kwargs()
        kwargs['message'] = Message.objects.last()
        kwargs['client'] = Client.objects.last()
        return kwargs

    def form_valid(self, form):
        send = form.save(commit=False)
        send.save()

        # Получаем объект сообщения
        message = send.message

        # Получаем список клиентов, связанных с сообщением
        clients = message.client_set.all()

        # Формируем тему и текст электронного письма
        subject = message.title
        body = message.text

        # Получаем список получателей электронного письма
        recipients = [client.email for client in clients]

        # Отправляем электронное письмо
        send_mail(
            subject=subject,
            message=body,
            from_email='dirtyslap@yandex.ru',
            recipient_list=recipients,
            fail_silently=False,
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('message:send_detail', kwargs={'pk': self.object.pk})


class SendUpdateView(UpdateView):
    model = Message
