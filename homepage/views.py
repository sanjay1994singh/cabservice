from django.shortcuts import render
from car_and_rent.models import CarsRent
from hotels.models import Hotels
from tourist_places.models import TouristPlace
from videos.models import Video


def homepage(request):
    cars = CarsRent.objects.all()
    place = TouristPlace.objects.all()
    hotel = Hotels.objects.all()
    video = Video.objects.all()
    context = {
        'cars': cars,
        'place': place,
        'hotel': hotel,
        'video': video,
    }
    return render(request, 'index-4.html', context)
