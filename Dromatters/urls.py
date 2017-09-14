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
from drought.models import RF
from drought import views
import re
import requests
import os
import django
from threading import Timer
from django.views.generic import TemplateView, RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

apipatterns = [
    url(r'^AllData/$', views.AllData.as_view()),
    url(r'^RegionData/$', views.RegionData.as_view()),
]

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=r'data/')),
    url(r'^data/$', TemplateView.as_view(template_name="data.html")),
    url(r'^region/$', TemplateView.as_view(template_name="region.html")),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += format_suffix_patterns(apipatterns)

# os.environ.update({"DJANGO_SETTINGS_MODULE": "Dromatters.settings"})
os.environ['DJANGO_SETTINGS_MODULE'] = 'Dromatters.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dromatters.settings")
django.setup()

pages = ['1', '2', '3', '4', '5', '6', '7']
init_url = "http://www.data.ac.cn/zrzy/ntBA02.asp"

CITYS_CNS = {u'Beijing': "北京      ", u'Tianjin': "天津      ", u'Hebei': "河北      ", u'Shanxi': "山西      ",
             u'Neimenggu': "内蒙古    ", u'Liaoning': "辽宁      ", u'Jilin': "吉林      ", u'Heilongjiang': "黑龙江    ",
             u'Jiangsu': "江苏      ", u'Anhui': "安徽      ", u'Shandong': "山东      ", u'Henan': "河南      ",
             u'Shaanxi': "陕西      ", u'Gansu': "甘肃      ", u'Qinghai': "青海      ", u'Ningxia': "宁夏      ",
             u'Xinjiang': "新疆      "}

CITYS_CNSS = {u'Beijing': "北京", u'Tianjin': "天津", u'Hebei': "河北", u'Shanxi': "山西", u'Neimenggu': "内蒙古",
              u'Liaoning': "辽宁", u'Jilin': "吉林", u'Heilongjiang': "黑龙江", u'Jiangsu': "江苏", u'Anhui': "安徽",
              u'Shandong': "山东", u'Henan': "河南", u'Shaanxi': "陕西", u'Gansu': "甘肃", u'Qinghai': "青海", u'Ningxia': "宁夏",
              u'Xinjiang': "新疆"}


def get_info():
    a = 0
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
                    city = CITYS_CNSS[key]
                    qset = RF.objects.filter(cityName=city, Year=y)
                    if qset:
                        continue
                    RF.objects.create(cityName=city, stationIndex=0)
                    obj = RF.objects.get(cityName=city, stationIndex=0)
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
    fix()


def fix():
    for y, x in CITYS_CNSS.items():
        obj = RF.objects.get(cityName=x, Year=1996)
        area = obj.Area
        rain = obj.Precipitation
        com = 1+(obj.Comparing/100)
        ave = rain/com
        obj.save()
        obj = RF.objects.get(cityName=x, Year=1997)
        obj.Area = area
        obj.save()
        obj = RF.objects.get(cityName=x, Year=1998)
        obj.Area = area
        pre = round((obj.totalPre/area)*10, 1)
        obj.Precipitation = pre
        obj.Comparing = round((pre-ave)*100/ave, 1)
        obj.save()
        obj = RF.objects.get(cityName=x, Year=1999)
        obj.Area = area
        obj.Comparing = round((obj.Precipitation-ave)*100/ave, 1)
        obj.save()
    makelevel()


def makelevel():
    qset = RF.objects.all()
    for x in qset:
        com = x.Comparing
        if x.level:
            continue
        if com > -15:
           x.level = "无旱"
        elif -30 < com <= -15:
           x.level = "轻旱"
        elif -40 < com <= -30:
            x.level = "中旱"
        elif -45 < com <= -40:
            x.level = "重旱"
        elif com <= -45:
            x.level = "特旱"
        x.save()
    print("finished!")

Timer(0, get_info).start()
