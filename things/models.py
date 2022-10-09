from django.db import models

# Creation of model Thing which represent a table in the db.
class Thing(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    



