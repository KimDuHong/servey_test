from django.contrib import admin
from .models import servey

# Register your models here.
@admin.register(servey)
class ServeyAdmin(admin.ModelAdmin):
    list_display = ("title",)
