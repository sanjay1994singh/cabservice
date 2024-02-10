from django.urls import path
from . import views

urlpatterns = [
    path('submit_detail/', views.submit_detail, name='submit_detail'),
]
