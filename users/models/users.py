from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models.managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Никнейм', max_length=64, unique=True, null=True, blank=True
    )
    email = models.EmailField(verbose_name='Почта', unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(verbose_name='Телефон', unique=True, null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} ({self.pk})'