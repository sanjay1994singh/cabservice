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


def hotels(request):
    hotel = Hotels.objects.all()
    context = {
        'hotel': hotel,
    }
    return render(request, 'hotel.html', context)


def book_cab(request):
    return render(request, 'book_cab.html')


def tourist_place(request):
    place = TouristPlace.objects.all()
    context = {
        'place': place,
    }
    return render(request, 'tourist_place.html', context)


def videos(request):
    video = Video.objects.all()
    context = {
        'video': video,
    }
    return render(request, 'videos.html', context)


def contact_us(request):
    return render(request, 'contact_us.html')
