from django.db import models

from .validators import validate_number


class Client(models.Model):
    number = models.CharField(max_length=11, validators=[validate_number], null=False, blank=False)
    code = models.CharField(max_length=3, null=False, blank=False)
    tag = models.CharField(max_length=26, null=False, blank=False)
    timezone = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f'Client {self.id}'



