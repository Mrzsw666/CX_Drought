from django.db import models

# Create your models here.


class RFBeijing(models.Model):    #北京
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20, null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)


class RFTianjin(models.Model):    #天津
    pass


class RFHebei(models.Model):      #河北
    pass


class RFShanxi(models.Model):     #山西
    pass


class RFNeimenggu(models.Model):  #内蒙古
    pass


class RFLiaoning(models.Model):   #辽宁
    pass


class RFJilin(models.Model):      #吉林
    pass


class RFHeilongjiang(models.Model): #黑龙江
    pass


class RFJiangsu(models.Model):     #江苏
    pass


class RFAnhui(models.Model):      #安徽
    pass


class RFShandong(models.Model):   #山东
    pass


class RFHenan(models.Model):      #河南
    pass


class RFShaanxi(models.Model):    #陕西
    pass


class RFGansu(models.Model):      #甘肃
    pass


class RFQinghai(models.Model):    #青海
    pass


class RFNingxia(models.Model):    #宁夏
    pass


class RFXinjiang(models.Model):   #新疆
    pass
