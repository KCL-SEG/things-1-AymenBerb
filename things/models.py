from enum import unique
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Creation of model Thing which represent a table in the db.
class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(default=0, unique=False, validator=[MinValueValidator(0), MaxValueValidator(100)])




