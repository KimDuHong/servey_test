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


# import plotly.express as px
# import pandas as pd
# from django.shortcuts import render
# from collections import defaultdict
# from result.models import Result
# from django.db.models import Max
# from result.serializers import ResultCountSerializer


# def bar_chart(request):
#     all_result = servey.objects.all()
#     serializer = ServeyCountSerializer(all_result, many=True)
#     result = Result.objects.all()
#     all_count = 0
#     max_count = 0
#     for i in result:
#         if max_count < i.count:
#             max_count = i.count
#         all_count += i.count
#     max_mbti = Result.objects.get(count=max_count)
#     chart_data = []
#     # print(chart_data == list(serializer.data))
#     # print(chart_data)
#     for i in serializer.data:
#         dic = {}
#         dic["first_answer"] = i["first_answer"]
#         dic["second_answer"] = i["second_answer"]
#         dic["first_count"] = i["first_count"]
#         dic["second_count"] = i["second_count"]
#         chart_data.append(dic)
#     percent = int(max_count / all_count * 100)

#     all_mbti_result = Result.objects.all()
#     serializer = ResultCountSerializer(all_mbti_result, many=True)
#     mbti_chart_data = []
#     # print(chart_data == list(serializer.data))
#     # print(chart_data)
#     for i in serializer.data:
#         dic = {}
#         dic["mbti"] = i["mbti"]
#         dic["count"] = i["count"]
#         mbti_chart_data.append(dic)
#     print(mbti_chart_data)
#     return render(
#         request,
#         "bar_chart.html",
#         {
#             "chart_data": chart_data,
#             "max_mbti": max_mbti,
#             "all_count": all_count,
#             "max_count": max_count,
#             "percent": percent,
#             "mbti_chart_data": mbti_chart_data,
#         },
#     )
