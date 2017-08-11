from django.db import models

# Create your models here.


class RF(models.Model):    #北京
    index = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=20, null=True)
    stationIndex = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)
    Area = models.FloatField(null=True)
    Precipitation = models.IntegerField(null=True)
    totalPre = models.FloatField(null=True)
    Comparing = models.FloatField(null=True)


class Beijing(RF):
    pass


class RFTianjin(RF):    #天津
    pass


class RFHebei(RF):      #河北
    pass


class RFShanxi(RF):     #山西
    pass


class RFNeimenggu(RF):  #内蒙古
    pass


class RFLiaoning(RF):   #辽宁
    pass


class RFJilin(RF):      #吉林
    pass


class RFHeilongjiang(RF): #黑龙江
    pass


class RFJiangsu(RF):     #江苏
    pass


class RFAnhui(RF):      #安徽
    pass


class RFShandong(RF):   #山东
    pass


class RFHenan(RF):      #河南
    pass


class RFShaanxi(RF):    #陕西
    pass


class RFGansu(RF):      #甘肃
    pass


class RFQinghai(RF):    #青海
    pass


class RFNingxia(RF):    #宁夏
    pass


class RFXinjiang(RF):   #新疆
    pass
