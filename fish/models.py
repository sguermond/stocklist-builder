from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import pgettext


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Species(BaseModel):
    """Fish species indexed by scientific name"""
    class Meta:
        verbose_name = pgettext("species singular", "species")
        verbose_name_plural = pgettext("species plural", "species")

    species = models.CharField(max_length=50)
    family = models.CharField(max_length=20)
    group_size = models.IntegerField(default=1)

    # tank size
    length = models.IntegerField(default=20)
    depth = models.IntegerField(default=20)
    height = models.IntegerField(default=20)
    volume = models.FloatField(default=10)

    # parameters
    temp_low = models.FloatField()
    temp_high = models.FloatField()
    ph_low = models.FloatField()
    ph_high = models.FloatField()

    def __str__(self):
        return self.species

    def stale(self):
        return self.updated_at < timezone.now() - timedelta(weeks=1)


class Common(BaseModel):
    """Common name of species"""
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Alternate(BaseModel):
    """Alternate scientific name"""
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.species, self.name


class Reference(BaseModel):
    """Link to outside factsheet for species"""
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)