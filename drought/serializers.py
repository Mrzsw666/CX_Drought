from rest_framework import serializers

from drought.models import RF


class RFSerializers(serializers.ModelSerializer):
    class Meta:
        model = RF
        fields = ('index', 'cityName', 'stationIndex', 'Year', 'Area', 'Precipitation', 'totalPre', 'Comparing', 'level')
