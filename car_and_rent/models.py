from django.db import models


# Create your models here.
class CarsRent(models.Model):
    car_img = models.ImageField(upload_to='cars_image', blank=True)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    base_rate = models.IntegerField(null=True, blank=True)
    car_rate_with_km = models.IntegerField(null=True, blank=True)
    car_passenger = models.IntegerField(null=True, blank=True)
    air_conditioner = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.car_name

    class Meta:
        db_table = 'cars_rent'
