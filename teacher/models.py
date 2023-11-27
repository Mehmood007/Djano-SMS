from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    
