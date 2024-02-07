from django.contrib import admin
from .models import CarsRent


class CarsRentAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_name', 'base_rate', 'car_rate_with_km', 'car_passenger', 'air_conditioner')
    list_filter = ('id', 'car_name', 'base_rate', 'car_rate_with_km', 'car_passenger', 'air_conditioner')


# Register your models here.

admin.site.register(CarsRent, CarsRentAdmin)
