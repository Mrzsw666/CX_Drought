# Create your views here.

from drought.models import RFBeijing, RFTianjin, RFHebei, RFShanxi, RFNeimenggu, RFLiaoning, RFJilin, \
    RFHeilongjiang, RFJiangsu, RFAnhui, RFShandong, RFHenan, RFShaanxi, RFGansu, RFQinghai, RFNingxia, RFXinjiang
from django.shortcuts import render
import tensorflow


CITYS_RFDB = {u'Beijing': RFBeijing, u'Tianjin': RFTianjin, u'RFHebei': RFHebei, u'Shanxi': RFShanxi,
              u'Neimenggu': RFNeimenggu, u'Liaoning': RFLiaoning, u'Jilin': RFJilin, u'RFHeilongjiang': RFHeilongjiang,
              u'Jiangsu': RFJiangsu, u'Anhui': RFAnhui, u'Shandong': RFShandong, u'Henan': RFHenan, u'Shaanxi': RFShanxi,
              u'Gansu': RFGansu, u'Qinghai': RFQinghai, u'Ningxia':RFNingxia, u'Xinjiang': RFXinjiang}


def main(request):
    llist = []
    dlist = []
    try:
        for i in (1995, 1999):
            for x in CITYS_RFDB:
                qset = x.object.filter(Year=i)
                llist.append(x)
                dlist.append(qset.Year)
                dlist.append(qset.Precipitation)
        return render(request, 'main.html', {'llist': llist, 'dlist':dlist})
    except Exception as e:
        print(e)
        return render(request, 'main.html')
