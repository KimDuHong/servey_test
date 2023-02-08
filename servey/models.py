from django.db import models
from common.models import CommonModel

# Create your models here.
class servey(CommonModel):
    title = models.TextField(max_length=100)
    first_answer = models.TextField(max_length=100)
    second_answer = models.TextField(max_length=100)
    branch = models.CharField(max_length=4)
    first_count = models.PositiveIntegerField()
    second_count = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title
