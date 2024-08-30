from django.db import models

# Create your models here.


class Fertilizer(models.Model):
    fertilizer_name = models.CharField(max_length=255)
    nitrogen = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False)
    phosphorus = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False)
    potassium = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False)
    poster = models.ImageField()
