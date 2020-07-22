from django.db import models
from django.utils import timezone
# Create your models here.



class StMaroc(models.Model):
    """docstring forStMaroc."""
    date=models.DateField(default=timezone.now())
    cases=models.FloatField(default='0')
    recov=models.FloatField(default='0')
    death=models.FloatField(default='0')
    tests=models.FloatField(default='0')
    casesD=models.FloatField(default='0')
    recovD=models.FloatField(default='0')
    deathD=models.FloatField(default='0')
    testsD=models.FloatField(default='0')
    def __str__(self):
        return '{} {}'.format(self.date,self.cases)
