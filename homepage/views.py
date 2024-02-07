from django.shortcuts import render

from car_and_rent.models import CarsRent


def homepage(request):
    cars = CarsRent.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'index-4.html', context)
