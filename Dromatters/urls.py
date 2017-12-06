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
from django.conf import settings
from drought import views

import urllib
import urllib.request
import chardet
import re
import requests
import csv
import os
import sys
from threading import Timer
from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
import xlrd, pymysql

apipatterns = [
    url(r'^AllData/$', views.AllData.as_view()),
    url(r'^RegionData/$', views.RegionData.as_view()),
]

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=r'data/')),
    url(r'^data/$', TemplateView.as_view(template_name="data.html")),
    url(r'^region/$', TemplateView.as_view(template_name="region.html")),
    url(r'^show/$', TemplateView.as_view(template_name="show.html")),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += format_suffix_patterns(apipatterns)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

CITYS_CNS = {u'北京': "bjave", u'上海': "shave", u'广州': "gzave"}


def get_pic():
    page = urllib.request.urlopen("http://www.cwb.gov.tw/V7/observe/satellite/Sat_EA.htm#")
    html = page.read()
    encode_type = chardet.detect(html)
    html = html.decode(encode_type['encoding'])
    print(html)
    reg = r's1p/(.*?)\" />'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    for link in imglist:
        html_url = 'http://www.cwb.gov.tw/V7/observe/satellite/Data/s1p/' + str(link)
        print(html_url)
        curPath = os.getcwd()
        fatherPath = os.path.dirname(curPath)
        filename = os.path.basename(html_url)
        urllib.request.urlretrieve(html_url, fatherPath + "/front_end/css/images/" + filename)


def get_info():
    data = xlrd.open_workbook("./static/datasheet.xlsx")
    table = data.sheet_by_index(0)
    qset = RF.objects.all()
    if qset:
        print("finish!")
        return
    for i in range(0, 3):
        cn = table.cell_value(i, 0)
        for j in range(1, 13):
            ave = float(table.cell_value(i, j))
            obj = RF.objects.create(cityName=CITYS_CNS[cn], month=j, rainfall=ave)
            obj.save()
    for i in range(3, table.nrows):
        cityname = table.cell_value(i, 0)
        year = int(table.cell_value(i, 1))
        month = int(table.cell_value(i, 2))
        rainfall = float(table.cell_value(i, 3))
        obj = RF.objects.create(cityName=cityname, year=year, month=month, rainfall=rainfall)
        obj.save()
    makelevel()


def makelevel():
    for i, j in CITYS_CNS.items():
        obj = RF.objects.filter(cityName=i)
        for o in obj:
            m = o.month
            ob = RF.objects.get(cityName=j, month=m)
            ave = ob.rainfall
            rf = o.rainfall
            temp = (rf - ave) / ave
            if temp > -0.15:
                o.level = "无旱"
            elif temp > -0.3:
                o.level = "轻旱"
            elif temp > -0.4:
                o.level = "中旱"
            elif temp > -0.45:
                o.level = "重旱"
            else:
                o.level = "特旱"
            o.save()
    print("finish!")


def go():
    o = sys.argv
    if o[1] == "runserver":
        Timer(0, get_info).start()
        #Timer(0, get_pic).start()

Timer(0, go).start()
