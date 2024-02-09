from django.shortcuts import render

from car_and_rent.models import CarsRent
from hotels.models import Hotels
from tourist_places.models import TouristPlace


def homepage(request):
    cars = CarsRent.objects.all()
    place = TouristPlace.objects.all()
    hotel = Hotels.objects.all()
    context = {
        'cars': cars,
        'place': place,
        'hotel': hotel,
    }
    return render(request, 'index-4.html', context)
