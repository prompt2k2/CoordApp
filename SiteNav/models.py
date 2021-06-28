from django.db import models
from django.contrib.gis.db import models

class siteloc(models.Model):
    sitecode = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    location = models.PointField()
    manager = models.CharField(max_length=50)
    engineer = models.CharField(max_length=50)