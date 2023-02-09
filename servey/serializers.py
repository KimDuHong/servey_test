from rest_framework import serializers
from .models import servey


class ServeySerializers(serializers.ModelSerializer):
    class Meta:
        model = servey
        exclude = (
            "created_at",
            "updated_at",
            "first_count",
            "second_count",
        )


class ServeyCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = servey
        fields = (
            "branch",
            "first_count",
            "first_answer",
            "second_count",
            "second_answer",
        )
