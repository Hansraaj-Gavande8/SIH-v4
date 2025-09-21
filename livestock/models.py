import uuid
from django.db import models
from django.contrib.auth.models import User

class Farm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Livestock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    tag_number = models.CharField(max_length=50)
    species = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tag_number
