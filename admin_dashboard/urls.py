from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('',                        views.admin_home,         name='home'),
    path('users/',                  views.manage_users,       name='users'),
    path('users/toggle/<int:pk>/',  views.toggle_user_active, name='toggle_user'),
    path('produce/',                views.manage_produce,     name='produce'),
    path('produce/delete/<int:pk>/',
         views.delete_produce,     name='delete_produce'),
    path('orders/',                 views.manage_orders,      name='orders'),
]
