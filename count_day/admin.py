from django.contrib import admin
from .models import count_day

# Register your models here.


@admin.action(description="set all count Zero")
def reset_all(model_admin, request, results):
    for result in results:
        result.count = 0
        result.save()


@admin.register(count_day)
class KindAdmin(admin.ModelAdmin):
    actions = (reset_all,)
    list_display = (
        "day",
        "count",
        "created_at",
        "updated_at",
    )
    list_filter = ("day",)
