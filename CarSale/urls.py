from django.urls import path
from . import views

urlpatterns = [
	path('', views.Car_list, name='Car_list'),
]