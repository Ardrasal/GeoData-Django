from django.db import models

class LatLong(models.Model):
    latitude = models.DecimalField(null=True, max_digits=10, decimal_places=6)
    longitude = models.DecimalField(null=True, max_digits=10, decimal_places=6)
