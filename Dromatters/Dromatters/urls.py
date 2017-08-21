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
from drought.models import RFBeijing, RFTianjin, RFHebei, RFShanxi, RFNeimenggu, RFLiaoning, RFJilin, RFHeilongjiang, \
    RFJiangsu, RFAnhui, RFShandong, RFHenan, RFShaanxi, RFGansu, RFQinghai, RFNingxia, RFXinjiang
from drought.views import data
from drought.views import CITYS_RFDB
import re
import requests
import os
import django
from threading import Timer

urlpatterns = [
    url(r'^data/$', data, name="data"),
    url(r'^admin/', admin.site.urls),
]
os.environ['DJANGO_SETTINGS_MODULE'] = 'Dromatters.settings'
django.setup()


pages = ['1', '2', '3', '4', '5', '6', '7']

init_url = "http://www.data.ac.cn/zrzy/ntBA02.asp"

'''
def get_info():
    for cur_page in pages:
        payload = {'Page': cur_page}
        r = requests.get(init_url, params=payload)
        r.encoding = 'GBK'
        p1 = r"(?<=<TD>).+?(?=</TD>)"
        pattern = re.compile(p1)
        result = re.findall(pattern, r.text)
        a = 0
        for key in result:
            if a % 10 == 0:
                if result[a + 1] == "北京      ":
                    RFBeijing.objects.create(stationIndex=0)
                    obj = RFBeijing.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "天津      ":
                    RFTianjin.objects.create(stationIndex=0)
                    obj = RFTianjin.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "河北      ":
                    RFHebei.objects.create(stationIndex=0)
                    obj = RFHebei.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "山西      ":
                    RFShanxi.objects.create(stationIndex=0)
                    obj = RFShanxi.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "内蒙古    ":
                    RFNeimenggu.objects.create(stationIndex=0)
                    obj = RFNeimenggu.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "辽宁      ":
                    RFLiaoning.objects.create(stationIndex=0)
                    obj = RFLiaoning.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "吉林      ":
                    RFJilin.objects.create(stationIndex=0)
                    obj = RFJilin.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "黑龙江    ":
                    RFHeilongjiang.objects.create(stationIndex=0)
                    obj = RFHeilongjiang.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "江苏      ":
                    RFJiangsu.objects.create(stationIndex=0)
                    obj = RFJiangsu.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "安徽      ":
                    RFAnhui.objects.create(stationIndex=0)
                    obj = RFAnhui.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "山东      ":
                    RFShandong.objects.create(stationIndex=0)
                    obj = RFShandong.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "河南      ":
                    RFHenan.objects.create(stationIndex=0)
                    obj = RFHenan.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "陕西      ":
                    RFShaanxi.objects.create(stationIndex=0)
                    obj = RFShaanxi.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "甘肃      ":
                    RFGansu.objects.create(stationIndex=0)
                    obj = RFGansu.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "青海      ":
                    RFQinghai.objects.create(stationIndex=0)
                    obj = RFQinghai.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "宁夏      ":
                    RFNingxia.objects.create(stationIndex=0)
                    obj = RFNingxia.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
                elif result[a + 1] == "新疆      ":
                    RFXinjiang.objects.create(stationIndex=0)
                    obj = RFXinjiang.objects.get(stationIndex=0)
                    obj.cityName = result[a + 1]
                    obj.stationIndex = int(result[a + 2])
                    obj.Year = int(result[a + 3])
                    obj.Area = float(result[a + 4])
                    obj.Precipitation = int(result[a + 5])
                    obj.totalPre = float(result[a + 6])
                    obj.Comparing = float(result[a + 8])
                    obj.save()
            a += 1'''

def get_info():
    for cur_page in pages:
        payload = {'Page': cur_page}
        r = requests.get(init_url, params=payload)
        r.encoding = 'GBK'
        p1 = r"(?<=<TD>).+?(?=</TD>)"
        pattern = re.compile(p1)
        result = re.findall(pattern, r.text)
    a = 0
    print(result)
    while a != 1340:
        for k in CITYS_RFDB:
            CITYS_RFDB[k].objects.create(stationIndex=0)
            obj = CITYS_RFDB[k].objects.get(stationIndex=0)
            obj.cityName = result[a + 1]
            obj.stationIndex = int(result[a + 2])
            obj.Year = int(result[a + 3])
            obj.Area = float(result[a + 4])
            obj.Precipitation = int(result[a + 5])
            obj.totalPre = float(result[a + 6])
            obj.Comparing = float(result[a + 8])
            obj.save()
            a+=10


Timer(0, get_info).start()
