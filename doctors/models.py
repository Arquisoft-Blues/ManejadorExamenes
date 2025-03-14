from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    identification = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
