import uuid

from django.db import models


# Create your models here.
class Attendee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.name)
    