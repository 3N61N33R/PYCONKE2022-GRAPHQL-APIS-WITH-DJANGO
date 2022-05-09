from django.db import models
from .abstract import TimeStampedModel

# Create your models here.

class Workshop(TimeStampedModel):
    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    location = models.CharField(max_length=100)