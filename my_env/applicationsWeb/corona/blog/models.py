from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class Blog(models.Model):
    """docstring for Blog."""
    user = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    nickname=models.CharField(max_length=100, default='THe Writter')
    titre=models.CharField(max_length=100)
    body=models.TextField()
    img=models.ImageField(upload_to='static',default='static/default.png')
    date=models.DateField(default=timezone.now())
    acitve=models.BooleanField(default=True)
    def __str__(self):
        return '{}'.format(self.titre)
