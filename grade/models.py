from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=30)


class Section(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)