from django import forms

class MessageForm(forms.Form):
    message_text = forms.CharField(label='', max_length=200)


class NewThreadForm(forms.Form):
    thread_title = forms.CharField(label='', max_length=40)