from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Species(BaseModel):
    """Fish species indexed by scientific name"""
    species = models.CharField(max_length=50)
    family = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=10)
    group_size = models.IntegerField(default=1)

    # tank size
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    volume = models.IntegerField()

    # parameters
    temp_low = models.IntegerField()
    temp_high = models.IntegerField()
    ph_low = models.IntegerField()
    ph_high = models.IntegerField()


class Common(BaseModel):
    """Common name of species"""
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Alternate(BaseModel):
    """Alternate scientific name"""
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Reference(BaseModel):
    """Link to outside factsheet for species"""
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)