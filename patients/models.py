from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    identification = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)