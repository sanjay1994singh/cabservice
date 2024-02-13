from django.db import models

# Create your models here.
from car_and_rent.models import CarsRent


class Place(models.Model):
    place_name = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.place_name

    class Meta:
        db_table = 'place'


class PlaceCarRent(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    car = models.ForeignKey(CarsRent, on_delete=models.CASCADE)
    seat = models.IntegerField(null=True, blank=True)
    rent = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.place.place_name) + ' ' + str(self.car.car_name)

    class Meta:
        db_table = 'place_car_rent'
