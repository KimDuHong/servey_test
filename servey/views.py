from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from common.models import CommonModel
from .models import servey
from .serializers import ServeySerializers, ServeyCountSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound

# Create your views here.


class serveyList(ModelViewSet):
    serializer_class = ServeySerializers
    queryset = servey.objects.all()


class serveyCountList(APIView):
    def get(self, request):
        countList = servey.objects.all()
        serializer = ServeyCountSerializer(countList, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     answer = request.data.get("answer")
    #     if not answer:
    #         raise ParseError("Answer is required")
    #     elif type(answer) == int:
    #         answer = str(answer)

    #     if len(answer) != 9:
    #         raise ParseError("Answer length must be 9")
    #     for i in answer:
    #         if i != "1" and i != "2":
    #             raise ParseError("Answer contains only 1 or 2")

    #     for idx, data in enumerate(answer):
    #         _servey = servey.objects.get(pk=idx + 1)

    #         if data == "1":
    #             _servey.first_count += 1
    #         else:
    #             _servey.second_count += 1
    #         _servey.save()

    #     countList = servey.objects.all()
    #     serializer = ServeyCountSerializer(countList, many=True)
    #     return Response(serializer.data)
