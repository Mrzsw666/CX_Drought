from django.db import models

# Create your models here.


class RF(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20, null=True)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    rainfall = models.FloatField(null=True)
    level = models.CharField(max_length=20, null=True)
