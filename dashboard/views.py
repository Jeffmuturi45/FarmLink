from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from produce.models import Produce
from orders.models import Order


@login_required
def farmer_dashboard(request):
    # Block buyers from accessing farmer dashboard
    if not request.user.is_farmer:
        messages.error(request, 'Access denied.')
        return redirect('dashboard:buyer')

    # All produce posted by this farmer
    my_produce = Produce.objects.filter(farmer=request.user)

    # All orders placed on this farmer's produce
    my_orders = Order.objects.filter(
        produce__farmer=request.user
    ).select_related('buyer', 'produce').order_by('-ordered_at')

    # Summary counts
    total_listings  = my_produce.count()
    active_listings = my_produce.filter(is_available=True).count()
    total_orders    = my_orders.count()
    pending_orders  = my_orders.filter(status='pending').count()

    return render(request, 'dashboard/farmer.html', {
        'my_produce':      my_produce,
        'my_orders':       my_orders,
        'total_listings':  total_listings,
        'active_listings': active_listings,
        'total_orders':    total_orders,
        'pending_orders':  pending_orders,
    })


@login_required
def buyer_dashboard(request):
    # Block farmers from accessing buyer dashboard
    if not request.user.is_buyer:
        messages.error(request, 'Access denied.')
        return redirect('dashboard:farmer')

    # All orders placed by this buyer
    my_orders = Order.objects.filter(
        buyer=request.user
    ).select_related('produce', 'produce__farmer').order_by('-ordered_at')

    # All available produce from all farmers
    market_produce = Produce.objects.filter(
        is_available=True
    ).exclude(
        farmer=request.user
    ).select_related('farmer')[:8]

    # Summary counts
    total_orders    = my_orders.count()
    pending_orders  = my_orders.filter(status='pending').count()
    accepted_orders = my_orders.filter(status='accepted').count()

    return render(request, 'dashboard/buyer.html', {
        'my_orders':       my_orders,
        'market_produce':  market_produce,
        'total_orders':    total_orders,
        'pending_orders':  pending_orders,
        'accepted_orders': accepted_orders,
    })