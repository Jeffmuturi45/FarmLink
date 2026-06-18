from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Add role, phone, location to the admin user form
    fieldsets = UserAdmin.fieldsets + (
        ('FarmLink Info', {'fields': ('role', 'phone', 'location')}),
    )
    list_display = ['username', 'email', 'role',
                    'phone', 'location', 'is_active']
    list_filter = ['role', 'is_active']
