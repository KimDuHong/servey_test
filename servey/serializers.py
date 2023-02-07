from rest_framework import serializers
from .models import servey


class ServeySerializers(serializers.ModelSerializer):
    class Meta:
        model = servey
        exclude = (
            "created_at",
            "updated_at",
        )
