from django import forms
from .models import MessageModel

class MessageForm(forms.ModelForm):
    pic_rel = forms.ImageField(label='', required=False)
    text = forms.CharField(label='', max_length=200)
    class Meta:
        model = MessageModel
        fields = ('text', 'pic_rel')


class NewThreadForm(forms.Form):
    thread_title = forms.CharField(label='', max_length=40)