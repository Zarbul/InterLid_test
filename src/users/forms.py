from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

from src.users.models import Manager, Employer


class ManagerCreationForm(forms.ModelForm):
    class Meta:
        model = Manager
        exclude = ("is_staff", "groups", "is_active", "is_superuser",
                   "user_permissions", "last_login", "date_joined")
        fields = ('username', 'password',)

        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }

    def save(self, commit=True):
        model = super().save(commit=False)
        # permission = Permission.objects.get(name='Can view parking')
        # model.user_permissions.add(permission)
        model.set_password(self.cleaned_data["password"])
        if commit:
            model.save()
            add_permission = Permission.objects.get(name='Can add parking')
            delete_permission = Permission.objects.get(name='Can delete parking')
            change_permission = Permission.objects.get(name='Can change parking')
            model.user_permissions.add(add_permission, delete_permission, change_permission)
        return model


class EmployerCreationForm(ManagerCreationForm):
    class Meta:
        model = Employer
        exclude = ("is_staff", "groups", "is_active", "is_superuser",
                   "user_permissions", "last_login", "date_joined")
        fields = ('username', 'password',)

        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }
