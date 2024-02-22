from django.shortcuts import render

from rate_list.models import Place, PlaceCarRent


def rate_list(request):
    place = Place.objects.all()
    rent_list = []
    for place in place:
        data_dict = {}
        data_dict['place_name'] = place.place_name
        place_car = PlaceCarRent.objects.filter(place_id=place.id)
        car_details_list = []
        for i in place_car:
            car_detail = {}
            car_detail['car_name'] = i.car.car_name
            car_detail['seat'] = i.seat
            car_detail['rent'] = i.rent
            car_details_list.append(car_detail)
        data_dict['car_details'] = car_details_list
        rent_list.append(data_dict)

    print(rent_list, '===============place_data')
    context = {
        'place': rent_list,
    }
    return render(request, 'rate_list.html', context)
