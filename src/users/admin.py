from django.contrib import admin

from src.users.models import Employer, Manager, AuthUser


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    pass


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass
