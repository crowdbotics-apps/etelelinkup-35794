from django.conf import settings
from django.db import models


class Entry(models.Model):
    "Generated Model"
    body = models.CharField(
        max_length=256,
    )
    title = models.CharField(
        max_length=256,
    )
