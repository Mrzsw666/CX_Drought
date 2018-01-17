from django.db import models

# Create your models here.


class RF(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20, null=True)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    rainfall = models.FloatField(null=True)
    level = models.CharField(max_length=20, null=True)


class Realtime(models.Model):
    cityName = models.CharField(max_length=20, null=True)
    tmp_max = models.IntegerField(null=True)
    tmp_min = models.IntegerField(null=True)
    cond_txt_d = models.CharField(max_length=20, null=True)
    cond_txt_n = models.CharField(max_length=20, null=True)
