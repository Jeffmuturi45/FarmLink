from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer', 'produce', 'quantity',
                    'total_price', 'status', 'ordered_at']
    list_filter = ['status']
    search_fields = ['buyer__username', 'produce__name']
    list_editable = ['status']
