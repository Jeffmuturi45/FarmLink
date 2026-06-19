from django.db import models
from decimal import Decimal
from accounts.models import CustomUser
from produce.models import Produce


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('accepted',  'Accepted'),
        ('rejected',  'Rejected'),
        ('completed', 'Completed'),
    ]

    buyer       = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    produce     = models.ForeignKey(Produce, on_delete=models.CASCADE, related_name='orders')
    quantity    = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    note        = models.TextField(blank=True)
    ordered_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-ordered_at']

    def __str__(self):
        return f"Order #{self.pk} — {self.buyer.username} → {self.produce.name}"

    def save(self, *args, **kwargs):
        if self.quantity and self.produce_id:
            self.total_price = Decimal(str(self.quantity)) * Decimal(str(self.produce.price))
        super().save(*args, **kwargs)