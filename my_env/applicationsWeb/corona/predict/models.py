from django.db import models

# Create your models here.


class Predict(models.Model):
    """docstring forPredict."""
    r0=models.FloatField(default=0)
    incubation=models.FloatField(default=0)
    percent_mild=models.FloatField(default=0)
    serial_interval=models.FloatField(default=0)
    fatality_rate=models.FloatField(default=0)
    percent_severe =models.FloatField(default=0)
    mild_recoveryMax= models.FloatField(default=0)
    mild_recoveryMin= models.FloatField(default=0)
    severe_recoveryMax=models.FloatField(default=0)
    severe_recoveryMin=models.FloatField(default=0)
    severe_deathMax=models.FloatField(default=0)
    severe_deathMin=models.FloatField(default=0)
    def __str__(self):
        return '{}'.format(self.r0)
