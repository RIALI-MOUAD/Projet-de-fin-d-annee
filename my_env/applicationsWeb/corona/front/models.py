from django.db import models
from django.utils import timezone
# Create your models here.

class FrontHome(models.Model):
    """docstring for FrontHome."""
    date=models.DateField(default=timezone.now())
    casconfirmed=models.CharField(max_length=100)
    casretablis=models.CharField(max_length=100)
    casmorts=models.CharField(max_length=100)
    casexclus=models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.id)
