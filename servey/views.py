from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import servey
from .serializers import ServeySerializers

# Create your views here.


class servey(ModelViewSet):
    serializer_class = ServeySerializers
    queryset = servey.objects.all()
