from turtle import mode

from django.contrib.auth.models import AbstractUser
from django.db import models


# Role choices
class Role(models.TextChoices):
    FARMER = 'farmer', 'Farmer'
    BUYER = 'buyer', 'Buyer'
    ADMIN = 'admin', 'Admin'


class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=10, choices=Role.choices, default=Role.FARMER)
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_photo = models.ImageField(
    upload_to='profiles/',
    blank=True,
    null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    # Helper properties for role checks in templates and views
    @property
    def is_farmer(self):
        return self.role == Role.FARMER

    @property
    def is_buyer(self):
        return self.role == Role.BUYER

    @property
    def is_admin_user(self):
        return self.role == Role.ADMIN
