# Create your views here.

from drought.models import RFBeijing, RFTianjin, RFHebei, RFShanxi, RFNeimenggu, RFLiaoning, RFJilin, \
    RFHeilongjiang, RFJiangsu, RFAnhui, RFShandong, RFHenan, RFShaanxi, RFGansu, RFQinghai, RFNingxia, RFXinjiang
from django.shortcuts import render
import tensorflow
from django.http import HttpResponseRedirect, Http404

CITYS_RFDB = {u'Beijing': RFBeijing, u'Tianjin': RFTianjin, u'RFHebei': RFHebei, u'Shanxi': RFShanxi,
              u'Neimenggu': RFNeimenggu, u'Liaoning': RFLiaoning, u'Jilin': RFJilin, u'Heilongjiang': RFHeilongjiang,
              u'Jiangsu': RFJiangsu, u'Anhui': RFAnhui, u'Shandong': RFShandong, u'Henan': RFHenan,
              u'Shaanxi': RFShaanxi,
              u'Gansu': RFGansu, u'Qinghai': RFQinghai, u'Ningxia': RFNingxia, u'Xinjiang': RFXinjiang}

# CITYS_CN = {'北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '安徽', '山东', '河南', '陕西', '甘肃', '青海', '宁夏', '新疆'}

CITYS_CNS = {u'Beijing': "北京", u'Tianjin': "天津", u'Hebei': "河北", u'Shanxi': "山西", u'Neimenggu': "内蒙古",
             u'Liaoning': "辽宁", u'Jilin': "吉林", u'Heilongjiang':"黑龙江", u'Jiangsu': "江苏", u'Anhui': "安徽",
             u'Shandong':"山东", u'Henan': "天津", u'Shaanxi': "陕西", u'Gansu': "甘肃", u'Qinghai':"青海",
             u'Ningxia': "宁夏", u'Xinjiang': "新疆"}


def redi(request):
    return HttpResponseRedirect('/data')


def data(request):
    llist = []
    dlist = []
    try:
        for x, y in CITYS_RFDB.items():
            qset = y.objects.all().order_by('Year')
            city_name = CITYS_CNS[x]
            llist.append(city_name)
            for v in qset:
                dlist.append(v)
        return render(request, 'data.html', {'statu': u"OK", 'llist': llist, 'dlist': dlist})
    except Exception as e:
        print(e)
        return render(request, 'data.html', {'statu': u"ERROR"})


def region(request):
    city_name = request.GET.get('city')
    obj = CITYS_RFDB[city_name]
    llist = []
    try:
        qset = obj.objects.all().order_by('Year')
        for v in qset:
            llist.append(v)
        return render(request, 'region.html', {'statu': u"OK", 'llist': llist})
    except Exception as e:
        print(e)
        return render(request, 'region.html', {'statu': u"ERROR"})


def knowledge(request):
    return render(request, 'knowledge.html', {'statu': "OK"})
