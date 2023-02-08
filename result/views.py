from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from servey.models import servey
from .serializers import ResultSerializer, ResultCountSerializer
from rest_framework.exceptions import NotFound, ParseError

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

    def post(self, request, mbti):
        mbti = mbti.upper()
        result = self.get_object(mbti)
        result.count += 1
        answer = request.data.get("answer")
        print(answer)
        if not answer:
            raise ParseError("Answer is required")
        elif type(answer) == int:
            answer = str(answer)

        if len(answer) != 9:
            raise ParseError("Answer length must be 9")
        for i in answer:
            if i != "1" and i != "2":
                raise ParseError("Answer contains only 1 or 2")

        for idx, data in enumerate(answer):
            servey_get = servey.objects.get(pk=idx + 1)

            if data == "1":
                servey_get.first_count += 1
            else:
                servey_get.second_count += 1
            servey_get.save()
        result.save()
        serializer = ResultSerializer(result)
        return Response(serializer.data)


class ResultCount(APIView):
    def get_object(self, mbti):
        try:
            return Result.objects.get(mbti=mbti)
        except Result.DoesNotExist:
            raise NotFound

    def get(self, request):
        result = Result.objects.all()
        all_count = sum(r.count for r in result)
        serializer = ResultCountSerializer(result, many=True)
        new_serializer_data = list(serializer.data)
        new_serializer_data.insert(0, {"all_count": all_count})
        return Response(new_serializer_data)

    # def post(self, request):
    #     request.data["mbti"] = request.data["mbti"].upper()
    #     serializer = ResultCountSerializer(data=request.data)
    #     if serializer.is_valid():
    #         if request.data.get("count") is True:
    #             result = Result.objects.get(mbti=request.data.get("mbti"))
    #             result.count += 1
    #             result.save()
    #             return Response(ResultCountSerializer(result).data)
    #         else:
    #             raise ParseError("Can't update count")
    #     else:
    #         return Response(serializer.errors, status=400)
