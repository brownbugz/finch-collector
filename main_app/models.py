from django.db import models
from django.urls import reverse

REFILLS = (
    ('Wi', 'Winter'),
    ('Sp', 'Spring'),
    ('Su', 'Summer'),
    ('Fa', 'Fall')
)

# Create your models here.
class Planner(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'planner_id': self.id})


class Accessory(models.Model):
    date = models.DateField()
    season = models.CharField(
        max_length=2,
        choices=REFILLS,
        default=REFILLS[0][0]
    )
    planner = models.ForeignKey(Planner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_refill_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
