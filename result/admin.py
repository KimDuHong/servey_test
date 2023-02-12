from django.contrib import admin
from .models import Result, Kind, Tendencies

# Register your models here.
@admin.action(description="set all count Zero")
def reset_all(model_admin, request, results):
    for result in results:
        result.count = 0
        result.save()


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    actions = (reset_all,)
    list_display = ("mbti", "kind", "count")
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
