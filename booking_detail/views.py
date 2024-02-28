from django.http import JsonResponse
from .models import BookingDetail
from datetime import datetime

from twilio.rest import Client
from django.conf import settings


# Create your views here.


def submit_detail(request):
    if request.method == 'POST':
        form = request.POST
        mobile = form.get('mobile')
        name = form.get('name')
        address = form.get('address')
        booking_date = form.get('date')
        time = form.get('time')
        car_name = form.get('car_name')
        passenger = form.get('passenger')
        booking_date = datetime.strptime(booking_date, "%y-%m-%d")
        obj = BookingDetail.objects.create(mobile=mobile,
                                           name=name,
                                           address=address,
                                           date=booking_date,
                                           time=time,
                                           car_name=car_name,
                                           passenger=passenger,
                                           )

        if obj:
            status = 1
        else:
            status = 0

        context = {
            'status': status,
        }
        return JsonResponse(context)
