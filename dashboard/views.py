from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from produce.models import Produce
from orders.models import Order


@login_required
def farmer_dashboard(request):
    if not request.user.is_farmer:
        messages.error(request, 'Access denied.')
        return redirect('dashboard:buyer')

    my_produce = Produce.objects.filter(
        farmer=request.user).order_by('-date_posted')

    my_orders = Order.objects.filter(
        produce__farmer=request.user
    ).select_related('buyer', 'produce').order_by('-ordered_at')

    return render(request, 'dashboard/farmer.html', {
        'my_produce':      my_produce,
        'my_orders':       my_orders,
        'total_listings':  my_produce.count(),
        'active_listings': my_produce.filter(is_available=True).count(),
        'total_orders':    my_orders.count(),
        'pending_orders':  my_orders.filter(status='pending').count(),
    })


@login_required
def buyer_dashboard(request):
    if not request.user.is_buyer:
        messages.error(request, 'Access denied.')
        return redirect('dashboard:farmer')

    my_orders = Order.objects.filter(
        buyer=request.user
    ).select_related('produce', 'produce__farmer').order_by('-ordered_at')

    market_produce = Produce.objects.filter(
        is_available=True
    ).exclude(
        farmer=request.user
    ).select_related('farmer').order_by('-date_posted')[:8]

    return render(request, 'dashboard/buyer.html', {
        'my_orders':       my_orders,
        'market_produce':  market_produce,
        'total_orders':    my_orders.count(),
        'pending_orders':  my_orders.filter(status='pending').count(),
        'accepted_orders': my_orders.filter(status='accepted').count(),
    })
