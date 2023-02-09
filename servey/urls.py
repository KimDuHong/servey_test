from django.urls import path
from . import views

# from .views import bar_chart

# urlpatterns = [
#     path("", views.Categories.as_view()),
#     path("<int:pk>", views.CategoryDetail.as_view()),
# ]

urlpatterns = [
    path(
        "",
        views.serveyList.as_view(
            {
                "get": "list",
                # "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",
        views.serveyList.as_view(
            {
                "get": "retrieve",
                # "put": "partial_update",
                # "delete": "destroy",
            }
        ),
    ),
    path("count", views.serveyCountList.as_view()),
    # path("bar_chart/", bar_chart, name="bar_chart"),
]
