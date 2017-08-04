from django.db import models

# Create your models here.
class beijing(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class tianjin(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class hebei(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class shanxi(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class neimenggu(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class liaoning(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class jilin(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class heilongjiang(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class jiangsu(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class anhui(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class shandong(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class henan(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class shaanxi(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class gansu(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class qinghai(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class ningxia(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)

class xinjiang(models.Model):
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20,null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)
