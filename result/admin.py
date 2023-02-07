from django.contrib import admin
from .models import Result, Kind, Tendencies

# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("mbti", "kind")
    list_filter = ("mbti",)


# Register your models here.
@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "surmmary",
    )


@admin.register(Tendencies)
class TendenciesAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    list_filter = ("name",)
