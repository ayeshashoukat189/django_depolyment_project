from django.db import models

# Create your models here.
from django.db import models

class Students(models.Model):
  StudentId = models.CharField(max_length=255)
  StudentName = models.CharField(max_length=255)
  Gender = models.CharField(max_length=255)
  Year = models.CharField(max_length=255)
  ClassId = models.CharField(max_length=255)
