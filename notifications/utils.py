from .models import Notification


def notify(recipient, title, message, notif_type='general'):
    Notification.objects.create(
        recipient=recipient,
        title=title,
        message=message,
        notif_type=notif_type,
    )
