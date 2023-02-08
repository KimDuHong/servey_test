from rest_framework import serializers
from .models import Result, Kind, Tendencies


class TendencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tendencies
        fields = ("name",)


class KindSerializers(serializers.ModelSerializer):
    tendency = TendencySerializer(many=True)

    class Meta:
        model = Kind
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    kind = KindSerializers(read_only=True)

    class Meta:
        model = Result
        fields = "__all__"


class ResultCountSerializer(serializers.ModelSerializer):
    count = serializers.CharField(read_only=True)

    class Meta:
        model = Result
        fields = (
            "count",
            "mbti",
        )
