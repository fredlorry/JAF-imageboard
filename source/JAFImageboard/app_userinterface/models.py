from django.db import models

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Create your models here.

class TopicModel(models.Model):
    """"Model for topic: id, name."""
    name = models.CharField(max_length=3)
    def __str__(self):
        return self.name

        
class ThreadModel(models.Model):
    """Model for thread: id, reference to topic."""

    title = models.CharField(max_length=64)

    tpc = models.ForeignKey(TopicModel,
                            on_delete = models.CASCADE,
                            verbose_name = "topic")
    
    def __str__(self):
        return str(self.id)

def get_path_for_pic(instance, filename):
    return id_generator() + '/' + filename

class MessageModel(models.Model):
    """ Model for message: reference to topic, thread and string for data."""
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    pic_rel = models.ImageField(verbose_name="picture related", default=None, upload_to=get_path_for_pic)
    author_ip = models.GenericIPAddressField()
    thr = models.ForeignKey(ThreadModel,
                            on_delete = models.CASCADE,
                            verbose_name="thread")
    tpc = models.ForeignKey(TopicModel,
                            on_delete = models.CASCADE,
                            verbose_name = "topic")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)