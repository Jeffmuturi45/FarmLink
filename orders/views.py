from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from produce.models import Produce
from notifications.utils import notify


@login_required
def place_order(request, produce_pk):
    if not request.user.is_buyer:
        messages.error(request, 'Only buyers can place orders.')
        return redirect('produce:list')

    produce = get_object_or_404(Produce, pk=produce_pk, is_available=True)

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        note = request.POST.get('note', '')
        try:
            quantity = float(quantity)
            if quantity <= 0:
                raise ValueError
            if quantity > float(produce.quantity):
                messages.error(
                    request, f'Only {produce.quantity} {produce.unit} available.')
                return redirect('produce:list')
        except (ValueError, TypeError):
            messages.error(request, 'Enter a valid quantity.')
            return redirect('produce:list')

        order = Order.objects.create(
            buyer=request.user,
            produce=produce,
            quantity=quantity,
            note=note,
        )

        # Notify farmer
        notify(
            recipient=produce.farmer,
            title='New Order Received',
            message=f'{request.user.username} ordered {quantity} {produce.unit} of {produce.name}.',
            notif_type='order_placed',
        )

        messages.success(
            request, f'Order placed for {produce.name}! Waiting for farmer to confirm.')
        return redirect('dashboard:buyer')

    return render(request, 'orders/place_order.html', {'produce': produce})


@login_required
def update_order_status(request, pk, action):
    order = get_object_or_404(Order, pk=pk, produce__farmer=request.user)

    if action == 'accept':
        order.status = 'accepted'
        notify(
            recipient=order.buyer,
            title='Order Accepted ✅',
            message=f'Your order for {order.produce.name} has been accepted by {request.user.username}.',
            notif_type='order_accepted',
        )
        messages.success(request, f'Order #{order.pk} accepted.')

    elif action == 'reject':
        order.status = 'rejected'
        notify(
            recipient=order.buyer,
            title='Order Rejected ❌',
            message=f'Your order for {order.produce.name} was rejected by {request.user.username}.',
            notif_type='order_rejected',
        )
        messages.warning(request, f'Order #{order.pk} rejected.')

    order.save()
    return redirect('dashboard:farmer')
