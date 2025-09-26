from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None  # We are not using username as the identifier
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)

    is_writer = models.BooleanField(
        default=False,
        verbose_name="Are you a writer?"
    )

    USERNAME_FIELD = 'email'  # ❌ You had `USERNAME_FIELDs`, which is incorrect
    REQUIRED_FIELDS = []  # No other fields required when creating a user

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} - {self.first_name} - {self.last_name}'
