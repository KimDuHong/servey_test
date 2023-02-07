from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from .serializers import ResultSerializer
from rest_framework.exceptions import NotFound

# Create your views here.


class Results(APIView):
    def get(self, request):
        result = Result.objects.all()
        serializer = ResultSerializer(result, many=True)
        return Response(serializer.data)


class ResultDetail(APIView):
    def get_object(self, mbti):
        try:
            return Result.objects.get(mbti=mbti)
        except Result.DoesNotExist:
            raise NotFound

    def get(self, request, mbti):
        mbti = mbti.upper()
        result = self.get_object(mbti)
        serializer = ResultSerializer(result)
        return Response(serializer.data)
