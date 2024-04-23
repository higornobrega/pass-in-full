import uuid

from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    details = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    maximum_attendees = models.PositiveIntegerField()
    
