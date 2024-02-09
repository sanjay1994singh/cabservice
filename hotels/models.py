from django.db import models


# Create your models here.
class Hotels(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='hotels', null=True, blank=True)
    lat = models.CharField(max_length=50, null=True, blank=True)
    long = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hotels'
