from django.conf import settings
from django.db import models


class Body(models.Model):
    "Generated Model"
    about = models.CharField(
        max_length=256,
    )
