from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import CustomUser
from produce.models import Produce
from orders.models import Order


@staff_member_required
def admin_home(request):
    return render(request, 'admin_dashboard/home.html', {
        'total_users':    CustomUser.objects.count(),
        'total_farmers':  CustomUser.objects.filter(role='farmer').count(),
        'total_buyers':   CustomUser.objects.filter(role='buyer').count(),
        'total_produce':  Produce.objects.count(),
        'total_orders':   Order.objects.count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'recent_users':   CustomUser.objects.order_by('-date_joined')[:8],
        'recent_orders':  Order.objects.select_related(
            'buyer', 'produce', 'produce__farmer'
        ).order_by('-ordered_at')[:10],
        'recent_produce': Produce.objects.select_related('farmer').order_by('-date_posted')[:8],
    })


@staff_member_required
def manage_users(request):
    users = CustomUser.objects.order_by('-date_joined')
    return render(request, 'admin_dashboard/users.html', {'users': users})


@staff_member_required
def toggle_user_active(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    user.is_active = not user.is_active
    user.save()
    return redirect('admin_dashboard:users')


@staff_member_required
def manage_produce(request):
    produce = Produce.objects.select_related('farmer').order_by('-date_posted')
    return render(request, 'admin_dashboard/produce.html', {'produce': produce})


@staff_member_required
def admin_delete_produce(request, pk):
    produce = get_object_or_404(Produce, pk=pk)
    produce.delete()
    return redirect('admin_dashboard:produce')


@staff_member_required
def manage_orders(request):
    orders = Order.objects.select_related(
        'buyer', 'produce', 'produce__farmer'
    ).order_by('-ordered_at')
    return render(request, 'admin_dashboard/orders.html', {'orders': orders})
