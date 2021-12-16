from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from src.parking.forms import ParkingOrderForm
from src.parking.models import Parking, ParkingOrder


class ParkingCreateView(PermissionRequiredMixin, generic.CreateView):
    login_url = '/auth/login'
    permission_required = 'parking.add_parking'
    model = Parking
    template_name = 'parking/parking_add.html'
    success_url = reverse_lazy('parking:list')
    fields = ('name', )


class ParkingListView(generic.ListView):
    model = Parking
    context_object_name = 'parkings'
    extra_context = {'orders': ParkingOrder.objects.all()}


class ParkingUpdateView(PermissionRequiredMixin, generic.UpdateView):
    login_url = '/auth/login'
    permission_required = 'parking.change_parking'
    template_name = 'parking/parking_add.html'
    model = Parking
    fields = '__all__'
    success_url = reverse_lazy('parking:list')


class ParkingDeleteView(PermissionRequiredMixin, generic.DeleteView):
    login_url = '/auth/login'
    permission_required = 'parking.delete_parking'
    template_name = 'parking/parking_delete.html'
    model = Parking
    success_url = reverse_lazy('parking:list')


class ParkingOrderView(generic.CreateView):
    form_class = ParkingOrderForm
    # model = ParkingOrder
    template_name = 'parking/parking_add.html'
    success_url = reverse_lazy('parking:list')
    # fields = ('place', 'start_date', 'end_date', 'employer', )
