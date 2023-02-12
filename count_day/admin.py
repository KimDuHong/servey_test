from django.contrib import admin
from .models import count_day

# Register your models here.
@admin.register(count_day)
class KindAdmin(admin.ModelAdmin):
    list_display = (
        "day",
        "count",
        "created_at",
        "updated_at",
    )
    list_filter = ("day",)
