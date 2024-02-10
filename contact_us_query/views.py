from django.http import JsonResponse
from django.shortcuts import render
from .models import ContactQuery


# Create your views here.
def contact_us(request):
    return render(request, 'contact_us.html')


def submit_query(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        mobile = form.get('mobile')
        email = form.get('email')
        address = form.get('address')
        subject = form.get('subject')
        message = form.get('message')

        obj = ContactQuery.objects.create(name=name,
                                          mobile=mobile,
                                          email=email,
                                          address=address,
                                          subject=subject,
                                          message=message,
                                          )

        if obj:
            status = 1
        else:
            status = 0
        context = {
            'status': status
        }
        return JsonResponse(context)
