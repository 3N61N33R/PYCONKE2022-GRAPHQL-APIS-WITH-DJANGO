from django.db import models

# Create your models here.
# TimeStampedModel

# Workshop

# fields - title,speaker, location

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    abstract = True

class Workshop(TimeStampedModel):
    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    location = models.CharField(max_length=100)