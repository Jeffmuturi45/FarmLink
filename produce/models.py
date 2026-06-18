from django.db import models
from accounts.models import CustomUser


class Produce(models.Model):
    # Category choices
    CATEGORY_CHOICES = [
        ('cereals',     'Cereals'),
        ('vegetables',  'Vegetables'),
        ('fruits',      'Fruits'),
        ('legumes',     'Legumes'),
        ('tubers',      'Tubers'),
        ('other',       'Other'),
    ]

    farmer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='produce')
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='other')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, default='kg')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text='Price per unit in KES')
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='produce/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.name} by {self.farmer.username}"
