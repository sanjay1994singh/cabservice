from django.db import models


# Create your models here.
class ContactQuery(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name + ' ' + self.mobile)

    class Meta:
        db_table = 'contact_query'
