from django.urls import path
from . import views


urlpatterns = [
    path("", views.Results.as_view()),
    path("@<str:mbti>", views.ResultDetail.as_view()),
]
