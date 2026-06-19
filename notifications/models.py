from django.db import models
from accounts.models import CustomUser


class Notification(models.Model):
    TYPE_CHOICES = [
        ('order_placed',   'Order Placed'),
        ('order_accepted', 'Order Accepted'),
        ('order_rejected', 'Order Rejected'),
        ('general',        'General'),
    ]

    recipient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='notifications')
    notif_type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default='general')
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notif → {self.recipient.username}: {self.title}"
