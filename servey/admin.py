from django.contrib import admin
from .models import servey

# Register your models here.


@admin.action(description="set all count Zero")
def reset_all(model_admin, request, results):
    for result in results:
        result.first_count, result.second_count = 0, 0
        result.save()


@admin.register(servey)
class ServeyAdmin(admin.ModelAdmin):
    actions = (reset_all,)
    list_display = (
        "title",
        "first_count",
        "second_count",
    )
