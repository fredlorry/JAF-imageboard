from django.db import models

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

class MessageModel(models.Model):
    """ Model for message: reference to topic, thread and string for data."""
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # pic_rel = models.ImageField(verbose_name="picture related")
    author_ip = models.GenericIPAddressField()
    thr = models.ForeignKey(ThreadModel,
                            on_delete = models.CASCADE,
                            verbose_name="thread")
    tpc = models.ForeignKey(TopicModel,
                            on_delete = models.CASCADE,
                            verbose_name = "topic")
    def __str__(self):
        return str(self.id)