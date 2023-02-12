from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from servey.models import servey
from .serializers import ResultSerializer, ResultCountSerializer
from rest_framework.exceptions import NotFound, ParseError
from count_day.models import count_day
from django.utils import timezone
from count_day.models import count_day

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
        now = timezone.now()
        all_result = Result.objects.all()
        all_count = 0
        for i in all_result:
            all_count += i.count

        try:
            day = count_day.objects.get(day=now)
            day.count = all_count
            day.save()
        except count_day.DoesNotExist:
            count_day.objects.create(day=now, count=all_count)

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


from django.shortcuts import render
from .models import Result, Kind
from .serializers import ResultCountSerializer
from servey.serializers import ServeyCountSerializer


def bar_chart(request):
    all_result = servey.objects.all()
    serializer = ServeyCountSerializer(all_result, many=True)
    result = Result.objects.all()
    all_count = 0
    max_count = 0
    for i in result:
        if max_count < i.count:
            max_count = i.count
        all_count += i.count
    print(max_count)
    max_mbti = Result.objects.get(count=max_count)
    chart_data = []
    # print(chart_data == list(serializer.data))
    # print(chart_data)
    for i in serializer.data:
        dic = {}
        dic["first_answer"] = i["first_answer"]
        dic["second_answer"] = i["second_answer"]
        dic["first_count"] = i["first_count"]
        dic["second_count"] = i["second_count"]
        chart_data.append(dic)
    percent = int(max_count / all_count * 100)

    all_mbti_result = Result.objects.all()
    serializer = ResultCountSerializer(all_mbti_result, many=True)
    mbti_chart_data = []
    # print(chart_data == list(serializer.data))
    # print(chart_data)
    for i in serializer.data:
        dic = {}
        dic["mbti"] = i["mbti"]
        dic["count"] = i["count"]
        mbti_chart_data.append(dic)
    now = timezone.now()
    lastest_mbti_result = Result.objects.all().order_by("-updated_at")[:2]
    lastest_list = {
        int(str((now - i.updated_at).seconds)): [i.mbti, i.kind.kind]
        for i in lastest_mbti_result
    }
    count_day_list = sorted(
        [[str(i.day), i.count] for i in count_day.objects.all()], reverse=True
    )
    print(count_day_list)

    return render(
        request,
        "bar_chart.html",
        {
            "chart_data": chart_data,
            "max_mbti": max_mbti,
            "all_count": all_count,
            "max_count": max_count,
            "percent": percent,
            "kind": max_mbti.kind,
            "latest_mbti": lastest_list,
            "mbti_chart_data": mbti_chart_data,
            "count_day_list": count_day_list,
        },
    )
