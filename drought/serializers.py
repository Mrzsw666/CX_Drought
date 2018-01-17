from rest_framework import serializers

from drought.models import RF, Realtime


class RFSerializers(serializers.ModelSerializer):
    class Meta:
        model = RF
        fields = ('index', 'cityName', 'year', 'month', 'rainfall', 'level')


class TQSerializers(serializers.ModelSerializer):
    class Meta:
        model = Realtime
        fields = ('cityName', 'tmp_min', 'tmp_max', 'cond_txt_d', 'cond_txt_n')
