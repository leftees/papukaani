from django.db import models
from django.db.models.signals import pre_init

class Creature(models.Model):
    name = models.CharField(max_length=300)

class MapPoint(models.Model):
    creature = models.ForeignKey(Creature)
    timestamp = models.DateTimeField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9)  # decimals are important, float approximates
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    altitude = models.DecimalField(max_digits=8, decimal_places=3)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    public = models.BooleanField(default=False)

    class Meta:
        unique_together = (("creature", "timestamp"),)

