from django.urls import path
from . import views

urlpatterns = [
    path('contact_us/', views.contact_us, name='contact_us'),
    path('submit_query/', views.submit_query, name='submit_query'),
]
