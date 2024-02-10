from django.contrib import admin
from .models import ContactQuery


# Register your models here.
class ContactQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile', 'email')
    list_filter = ('id', 'name', 'mobile', 'email')


admin.site.register(ContactQuery, ContactQueryAdmin)
