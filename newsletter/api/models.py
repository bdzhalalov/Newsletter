from django.db import models
from django.utils import timezone

from clients.models import Client


class Newsletter(models.Model):
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    text = models.TextField(blank=False, null=False)
    filter = models.ManyToManyField(Client, related_name='filter')
    finish = models.DateTimeField(auto_now=False, auto_now_add=False)


class Message(models.Model):

    STATUS_CHOICES = [
        (0, 'created'),
        (1, 'in_progress'),
        (2, 'sent'),
        (3, 'failed'),
    ]

    sent_at = models.DateTimeField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=0)
    newsletter = models.OneToOneField(Newsletter, on_delete=models.DO_NOTHING)
    client = models.OneToOneField(Client, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        self.sent_at = timezone.now()
        return super(Message, self).save(*args, **kwargs)


