from django.db import models
import django
# Create your models here.



class Country(models.Model):
    """docstring forCountry."""
    name = models.CharField(max_length=100,primary_key = True)
    cases = models.FloatField(default=0)
    New_cases = models.FloatField(default=0)
    death = models.FloatField(default=0)
    New_Deaths= models.FloatField(default=0)
    Recover = models.FloatField(default=0)
    Active_Cases = models.FloatField(default=0)
    Serious =  models.FloatField(default=0)
    cases_million= models.FloatField(default=0)
    deaths_million= models.FloatField(default=0)
    tests = models.FloatField(default=0)
    test_million = models.FloatField(default=0)
    continent = models.CharField(max_length=100,default='world')
    date = models.DateTimeField(default = django.utils.timezone.now())
    def __str__(self):
        return '{}'.format(self.name)
