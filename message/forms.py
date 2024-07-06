from django import forms

from message.models import Message, Client


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email',)
