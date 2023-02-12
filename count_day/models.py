from django.db import models
from common.models import CommonModel

# Create your models here.
class count_day(CommonModel):
    day = models.DateField(unique=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return str(self.day)
