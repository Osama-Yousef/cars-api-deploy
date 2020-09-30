from django.urls import path

from .views import CarsList, CarDetails

urlpatterns = [
    path('', CarsList.as_view(), name='cars'), # localhost:8000/api/v1/cars
    path('<int:pk>/', CarDetails.as_view(), name='car_details') # localhost:8000/api/v1/cars/1
]