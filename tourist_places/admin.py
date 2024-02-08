from django.contrib import admin
from .models import TouristPlace


# Register your models here.
class TouristPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(TouristPlace, TouristPlaceAdmin)
