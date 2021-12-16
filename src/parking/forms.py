from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

from .models import ParkingOrder


class ParkingOrderForm(forms.ModelForm):
    class Meta:
        model = ParkingOrder
        fields = ('place', 'start_date', 'end_date', 'employer', )

        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }

    def save(self, *args, **kwargs):
        model = super().save(commit=False)
        model.place.used = True
        model.place.save()
        super().save(*args, **kwargs)
        return model

