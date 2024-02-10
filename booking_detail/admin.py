from django.contrib import admin
from .models import BookingDetail


# Register your models here.
class BookingDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile', 'name', 'address', 'date', 'time', 'car_name', 'passenger')
    list_filter = ('id', 'mobile', 'name', 'address', 'date', 'time', 'car_name', 'passenger')


admin.site.register(BookingDetail, BookingDetailAdmin)
