# Create your views here.

from drought.models import RF, Realtime
import tensorflow
from rest_framework import generics, permissions
from drought.serializers import RFSerializers, TQSerializers
from django.http import HttpResponse
import json

# CITYS_CN = {'北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '安徽', '山东', '河南', '陕西', '甘肃', '青海', '宁夏', '新疆'}

CITYS_CNS = {u'Beijing': "北京", u'Tianjin': "天津", u'Hebei': "河北", u'Shanxi': "山西", u'Neimenggu': "内蒙古",
             u'Liaoning': "辽宁", u'Jilin': "吉林", u'Heilongjiang': "黑龙江", u'Jiangsu': "江苏", u'Anhui': "安徽",
             u'Shandong': "山东", u'Henan': "天津", u'Shaanxi': "陕西", u'Gansu': "甘肃", u'Qinghai': "青海",
             u'Ningxia': "宁夏", u'Xinjiang': "新疆"}


class AllData(generics.ListAPIView):
    serializer_class = RFSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = RF.objects.all()
        dq = queryset.filter(cityName="bjave")
        dq.delete()
        dq = queryset.filter(cityName="shave")
        dq.delete()
        dq = queryset.filter(cityName="gzave")
        dq.delete()
        return queryset.order_by('year', 'month')


class RegionData(generics.ListAPIView):
    serializer_class = RFSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = RF.objects.all()
        city = self.request.query_params.get('cityName', None)
        year = self.request.query_params.get('year', None)
        if city is not None:
            queryset = queryset.filter(cityName=city, year=year)
        return queryset.order_by('year', 'month')


class TQ(generics.ListAPIView):
    serializer_class = TQSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Realtime.objects.all()
        return queryset


class GetForcast(generics.ListAPIView):
    serializer_class = TQSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = RF.objects.all()
        city = self.request.query_params.get('cityName', None)
        year = self.request.query_params.get('year', None)
        month = self.request.query_params.get('month', None)
        if city is not None:
            queryset = queryset.filter(cityName=city, year=year, month=month)
        return queryset
