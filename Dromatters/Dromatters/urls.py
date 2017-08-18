
"""Dromatters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

import os,django
os.environ['DJANGO_SETTINGS_MODULE'] = 'Dromatters.settings'
django.setup()
from drought import models
from drought.models import RFBeijing,RFTianjin,RFHebei,RFShanxi,RFNeimenggu,RFLiaoning,RFJilin,RFHeilongjiang,RFJiangsu,RFAnhui,RFShandong,RFHenan,RFShaanxi,RFGansu,RFQinghai,RFNingxia,RFXinjiang
import re
import requests
pages=['1','2','3','4','5','6','7']

init_url="http://www.data.ac.cn/zrzy/ntBA02.asp"
def get_info():
    for cur_page in pages:
        payload= {'Page':cur_page}
        r=requests.get(init_url,params=payload)
        r.encoding = 'GBK'
        p1=r"(?<=<TD>).+?(?=</TD>)"
        pattern=re.compile(p1)
        result=re.findall(pattern,r.text)
        a=0
        for key in result:
            if a%10==0:
                if result[a+1]=="北京      ":
                    models.RFBeijing.objects.create(stationIndex=0)
                    obj = models.RFBeijing.objects.get(stationIndex=0)
                    obj.cityName=result[a+1]
                    obj.stationIndex=int(result[a+2])
                    obj.Year=int(result[a+3])
                    obj.Area=float(result[a+4])
                    obj.Precipitation=int(result[a+5])
                    obj.totalPre=float(result[a+6])
                    obj.Comparing=float(result[a+8])
                    obj.save()
                elif result[a+1]=="天津      ":
                    models.RFTianjin.objects.create(stationIndex=0)
                    obj = models.RFTianjin.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="河北      ":
                    models.RFHebei.objects.create(stationIndex=0)
                    obj = models.RFHebei.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="山西      ":
                    models.RFShanxi.objects.create(stationIndex=0)
                    obj = models.RFShanxi.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="内蒙古    ":
                    models.RFNeimenggu.objects.create(stationIndex=0)
                    obj = models.RFNeimenggu.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="辽宁      ":
                    models.RFLiaoning.objects.create(stationIndex=0)
                    obj = models.RFLiaoning.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="吉林      ":
                    models.RFJilin.objects.create(stationIndex=0)
                    obj = models.RFJilin.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="黑龙江    ":
                    models.RFHeilongjiang.objects.create(stationIndex=0)
                    obj = models.RFHeilongjiang.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="江苏      ":
                    models.RFJiangsu.objects.create(stationIndex=0)
                    obj = models.RFJiangsu.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="安徽      ":
                    models.RFAnhui.objects.create(stationIndex=0)
                    obj = models.RFAnhui.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="山东      ":
                    models.RFShandong.objects.create(stationIndex=0)
                    obj = models.RFShandong.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="河南      ":
                    models.RFHenan.objects.create(stationIndex=0)
                    obj = models.RFHenan.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="陕西      ":
                    models.RFShaanxi.objects.create(stationIndex=0)
                    obj = models.RFShaanxi.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="甘肃      ":
                    models.RFGansu.objects.create(stationIndex=0)
                    obj = models.RFGansu.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="青海      ":
                    models.RFQinghai.objects.create(stationIndex=0)
                    obj = models.RFQinghai.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="宁夏      ":
                    models.RFNingxia.objects.create(stationIndex=0)
                    obj = models.RFNingxia.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a+1]=="新疆      ":
                    models.RFXinjiang.objects.create(stationIndex=0)
                    obj = models.RFXinjiang.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
            a+=1
