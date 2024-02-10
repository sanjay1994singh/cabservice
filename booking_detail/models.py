from django.db import models


# Create your models here.
class BookingDetail(models.Model):
    mobile = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    car_name = models.CharField(max_length=100, null=True, blank=True)
    passenger = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.mobile

    class Meta:
        db_table = 'booking_detail'
