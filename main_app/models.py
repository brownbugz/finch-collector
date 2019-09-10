from django.db import models
from django.urls import reverse

# Create your models here.
class Planner(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'planner_id': self.id})
