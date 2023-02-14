from django.db import models
from common.models import CommonModel

# Create your models here.
class Result(CommonModel):
    class mbtiChoice(models.TextChoices):
        ENTJ = ("ENTJ", "ENTJ")
        ENTP = ("ENTP", "ENTP")
        ENFJ = ("ENFJ", "ENFJ")
        ENFP = ("ENFP", "ENFP")
        ESTJ = ("ESTJ", "ESTJ")
        ESTP = ("ESTP", "ESTP")
        ESFJ = ("ESFJ", "ESFJ")
        ESFP = ("ESFP", "ESFP")
        INTJ = ("INTJ", "INTJ")
        INTP = ("INTP", "INTP")
        INFJ = ("INFJ", "INFJ")
        INFP = ("INFP", "INFP")
        ISTJ = ("ISTJ", "ISFJ")
        ISTP = ("ISTP", "ISTP")
        ISFJ = ("ISFJ", "ISFJ")
        ISFP = ("ISFP", "ISFP")

    mbti = models.CharField(max_length=4, choices=mbtiChoice.choices)
    count = models.PositiveIntegerField()
    kind = models.ForeignKey(
        "result.Kind",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="kinds",
    )

    def __str__(self) -> str:
        return self.mbti


class Kind(models.Model):
    class KindChoices(models.TextChoices):
        App = ("앱 개발자", "앱 개발자")
        Data = ("데이터 엔지니어", "데이터 엔지니어")
        Iot = ("사물인터넷 개발", "사물인터넷 개발")
        Sys = ("시스템 네트워크", "시스템 네트워크")
        Back = ("서버 / 백엔드", "서버 / 백엔드")
        Front = ("프론트엔드", "프론트엔드")
        Emb = ("임베디드 프로그래머", "임베디드 프로그래머")
        Game = ("게임 개발자", "게임 개발자")
        Sec = ("보안전문가", "보안전문가")

    kind = models.CharField(max_length=20, choices=KindChoices.choices)
    similar = models.CharField(max_length=20, choices=KindChoices.choices)
    worst = models.CharField(max_length=20, choices=KindChoices.choices)
    surmmary = models.CharField(max_length=50)
    tendency = models.ManyToManyField(
        "result.Tendencies",
        related_name="tendency",
    )
    content = models.TextField()

    def __str__(self) -> str:
        return self.kind


class Tendencies(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Tendency"
        verbose_name_plural = "Tendencies"

    def __str__(self) -> str:
        return self.name
