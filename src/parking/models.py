from django.db import models
from django.utils import timezone

from src.users.models import Employer


class Parking(models.Model):
    name = models.CharField('Parking name', max_length=50, default='Parking name')
    used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class ParkingOrder(models.Model):
    place = models.ForeignKey(Parking, on_delete=models.CASCADE)
    start_date = models.DateTimeField('Start Date', default=timezone.now)
    end_date = models.DateTimeField('End Date', default=timezone.now)
    employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.place} was booked by {self.employer}.'
