from django.contrib import admin

from src.parking.models import Parking, ParkingOrder


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    pass

@admin.register(ParkingOrder)
class ParkingOrderAdmin(admin.ModelAdmin):
    pass
