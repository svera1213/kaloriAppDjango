from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    cholestrol = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    sat_fat = models.FloatField(default=0)
    sugar = models.FloatField(default=0)

    def __str__(self):
        return self.name
