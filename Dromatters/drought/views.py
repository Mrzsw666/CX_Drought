# Create your views here.

from drought.models import RFBeijing, RFTianjin, RFHebei, RFShanxi, RFNeimenggu, RFLiaoning, RFJilin, \
    RFHeilongjiang, RFJiangsu, RFAnhui, RFShandong, RFHenan, RFShaanxi, RFGansu, RFQinghai, RFNingxia, RFXinjiang
from django.shortcuts import render
import tensorflow


CITYS_RFDB = {u'Beijing': RFBeijing, u'Tianjin': RFTianjin, u'RFHebei': RFHebei, u'Shanxi': RFShanxi,
              u'Neimenggu': RFNeimenggu, u'Liaoning': RFLiaoning, u'Jilin': RFJilin, u'RFHeilongjiang': RFHeilongjiang,
              u'Jiangsu': RFJiangsu, u'Anhui': RFAnhui, u'Shandong': RFShandong, u'Henan': RFHenan, u'Shaanxi': RFShaanxi,
              u'Gansu': RFGansu, u'Qinghai': RFQinghai, u'Ningxia':RFNingxia, u'Xinjiang': RFXinjiang}

# CITYS_CN = {'北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '安徽', '山东', '河南', '陕西', '甘肃', '青海', '宁夏', '新疆'}


def data(request):
    llist = []
    dlist = []
    try:
        for i in (1995, 1999):
            for x in CITYS_RFDB:
                city_note = CITYS_RFDB[x]
                qset = city_note.objects.all()
                for v in qset:
                    llist.append(x)
                    dlist.append(v.Year)
                    dlist.append(v.Area)
                    dlist.append(v.Precipitation)
                    dlist.append(v.totalPre)
                    dlist.append(v.Comparing)
        return render(request, 'data.html', {'llist': llist, 'dlist':dlist})
    except Exception as e:
        print(e)
        return render(request, 'data.html')
