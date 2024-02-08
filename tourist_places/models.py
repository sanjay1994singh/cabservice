from django.db import models


# Create your models here.
class TouristPlace(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='tourist_place', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tourist_place'
