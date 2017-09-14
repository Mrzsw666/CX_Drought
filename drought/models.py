from django.db import models

# Create your models here.


class RF(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20, null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)
    level = models.CharField(max_length=20, null=True)
