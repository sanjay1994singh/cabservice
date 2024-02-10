from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book_cab/', views.book_cab, name='book_cab'),
    path('hotels/', views.hotels, name='hotels'),
    path('tourist_place/', views.tourist_place, name='tourist_place'),
    path('videos/', views.videos, name='videos'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
