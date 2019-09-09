from django.db import models

# Create your models here.
class Planner(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'