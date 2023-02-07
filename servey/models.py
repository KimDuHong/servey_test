from django.db import models
from common.models import CommonModel

# Create your models here.
class servey(CommonModel):
    title = models.CharField(
        max_length=100,
    )
    first_answer = models.TextField(max_length=100)
    second_answer = models.TextField(max_length=100)
    image = models.ImageField(
        null=True,
        blank=True,
    )
    branch = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.title
