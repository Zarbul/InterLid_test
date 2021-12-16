
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'parking'

urlpatterns = [
    path('', views.ParkingListView.as_view(), name='list'),
    path('add/', views.ParkingCreateView.as_view(), name='add_parking'),
    path('add_order/', views.ParkingOrderView.as_view(), name='booking_parking'),
    path('edit/<int:pk>/', views.ParkingUpdateView.as_view(), name='edit_parking'),
    path('delete/<int:pk>/', views.ParkingDeleteView.as_view(), name='delete_parking'),
]
