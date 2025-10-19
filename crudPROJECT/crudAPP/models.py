from django.db import models
from django.db.models import Model


# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=255)
    email= models.EmailField()

    def __str__(self):
        return  self.name