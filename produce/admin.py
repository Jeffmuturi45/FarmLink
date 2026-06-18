from django.contrib import admin
from .models import Produce


@admin.register(Produce)
class ProduceAdmin(admin.ModelAdmin):
    list_display = ['name', 'farmer', 'category', 'quantity',
                    'unit', 'price', 'location', 'is_available', 'date_posted']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'farmer__username', 'location']
    list_editable = ['is_available']
