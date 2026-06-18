from django.urls import path
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

app_name = 'dashboard'


@login_required
def farmer_dashboard(request):
    return render(request, 'dashboard/farmer.html')


@login_required
def buyer_dashboard(request):
    return render(request, 'dashboard/buyer.html')


urlpatterns = [
    path('farmer/', farmer_dashboard, name='farmer'),
    path('buyer/', buyer_dashboard, name='buyer'),
]
