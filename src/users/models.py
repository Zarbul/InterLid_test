from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class AuthUser(AbstractUser):
    username = models.CharField("Username", blank=False, null=False, max_length=50, unique=True)
    # REQUIRED_FIELDS = ['password', ]
    USERNAME_FIELD = 'username'

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Manager(AuthUser):
    # user.user_permissions.add('parking.view_parking',
    #                           'parking.add_manager',
    #                           'parking.change_manager',
    #                           'parking.delete_manager',
    #                           'parking.view_manager')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class Employer(AuthUser):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
