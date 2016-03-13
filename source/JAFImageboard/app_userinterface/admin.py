from django.contrib import admin

# Register your models here.

from .models import TopicModel, ThreadModel, MessageModel

admin.site.register(TopicModel)
admin.site.register(ThreadModel)
admin.site.register(MessageModel)