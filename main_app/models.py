from django.db import models
from django.urls import reverse
from datetime import date

REFILLS = (
    ('Wi', 'Winter'),
    ('Sp', 'Spring'),
    ('Su', 'Summer'),
    ('Fa', 'Fall')
)

class Gadget(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gadgets_detail', kwargs={'pk': self.id})

class Planner(models.Model): 
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    gadgets = models.ManyToManyField(Gadget)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'planner_id': self.id})
    
    def accessorized_for_today(self):
        return self.accessory_set.filter(date=date.today()).count() >= len(REFILLS)


class Accessory(models.Model):
    date = models.DateField('accessory date')
    season = models.CharField(
        max_length=2,
        choices=REFILLS,
        default=REFILLS[0][0]
    )
    planner = models.ForeignKey(Planner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_season_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
