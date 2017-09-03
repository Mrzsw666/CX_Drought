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
from drought.views import data, redi, region, knowledge
import re
import requests
import os
import django
from threading import Timer

urlpatterns = [
    url(r'^$', redi, name="webroot"),
    url(r'^data/$', data, name="data"),
    url(r'region/$', region, name="region"),
    url(r'knowledge/', knowledge, name="knowledge"),
    url(r'^admin/', admin.site.urls),
]
# os.environ.update({"DJANGO_SETTINGS_MODULE": "Dromatters.settings"})
os.environ['DJANGO_SETTINGS_MODULE'] = 'Dromatters.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dromatters.settings")
django.setup()

pages = ['1', '2', '3', '4', '5', '6', '7']
init_url = "http://www.data.ac.cn/zrzy/ntBA02.asp"

CITYS_RFDB = {u'Beijing': RFBeijing, u'Tianjin': RFTianjin, u'Hebei': RFHebei, u'Shanxi': RFShanxi,
              u'Neimenggu': RFNeimenggu, u'Liaoning': RFLiaoning, u'Jilin': RFJilin, u'Heilongjiang': RFHeilongjiang,
              u'Jiangsu': RFJiangsu, u'Anhui': RFAnhui, u'Shandong': RFShandong, u'Henan': RFHenan,
              u'Shaanxi': RFShaanxi, u'Gansu': RFGansu, u'Qinghai': RFQinghai, u'Ningxia': RFNingxia,
              u'Xinjiang': RFXinjiang}

CITYS_CNS = {u'Beijing': "北京      ", u'Tianjin': "天津      ", u'Hebei': "河北      ", u'Shanxi': "山西      ",
             u'Neimenggu': "内蒙古    ", u'Liaoning': "辽宁      ", u'Jilin': "吉林      ", u'Heilongjiang': "黑龙江    ",
             u'Jiangsu': "江苏      ", u'Anhui': "安徽      ", u'Shandong': "山东      ", u'Henan': "河南      ",
             u'Shaanxi': "陕西      ", u'Gansu': "甘肃      ", u'Qinghai': "青海      ", u'Ningxia': "宁夏      ",
             u'Xinjiang': "新疆      "}


def get_info():
    a = 0
    cnt = 0
    for cur_page in pages:
        payload = {'Page': cur_page}
        r = requests.get(init_url, params=payload)
        r.encoding = 'GBK'
        p1 = r"(?<=<TD>).+?(?=</TD>)"
        pattern = re.compile(p1)
        result = re.findall(pattern, r.text)
        # print(result)
        while a != 1340:
            for key in CITYS_CNS:
                if CITYS_CNS[key] == result[a % 200 + 1]:
                    y = int(result[a % 200 + 3])
                    qset = CITYS_RFDB[key].objects.filter(Year=y)
                    if qset:
                        continue
                    CITYS_RFDB[key].objects.create(stationIndex=0)
                    obj = CITYS_RFDB[key].objects.get(stationIndex=0)
                    obj.cityName = result[a % 200 + 1]
                    obj.stationIndex = int(result[a % 200 + 2])
                    obj.Year = int(result[a % 200 + 3])
                    obj.Area = float(result[a % 200 + 4])
                    obj.Precipitation = int(result[a % 200 + 5])
                    obj.totalPre = float(result[a % 200 + 6])
                    obj.Comparing = float(result[a % 200 + 8])
                    obj.save()
                    break
            a += 10
            if a == 200 or a == 400 or a == 600 or a == 800 or a == 1000 or a == 1200:
                break
        print(cnt)
        cnt += 1
    fix()


def fix():
    for y, x in CITYS_RFDB.items():
        obj = x.objects.get(Year=1996)
        area = obj.Area
        rain = obj.Precipitation
        com = 1+(obj.Comparing/100)
        ave = rain/com
        obj.save()
        obj = x.objects.get(Year=1997)
        obj.Area = area
        obj.save()
        obj = x.objects.get(Year=1998)
        obj.Area = area
        pre = round((obj.totalPre/area)*10, 1)
        obj.Precipitation = pre
        obj.Comparing = round((pre-ave)*100/ave, 1)
        obj.save()
        obj = x.objects.get(Year=1999)
        obj.Area = area
        obj.Comparing = round((obj.Precipitation-ave)*100/ave, 1)
        obj.save()

Timer(0, get_info).start()
