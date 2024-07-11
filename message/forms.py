from django import forms

from message.models import Message, Client, Send


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email',)


class SendForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        message = kwargs.pop('message', None)
        client = kwargs.pop('client', None)
        super(SendForm, self).__init__(*args, **kwargs)
        if message:
            self.fields['message'].initial = message
        if client:
            self.fields['client'].initial = client

    class Meta:
        model = Send
        fields = ['date_and_time_of_first_send', 'periodicity', 'status', 'client', 'message']
