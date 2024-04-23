import uuid

from django.db import models


# Create your models here.
class CheckIn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
