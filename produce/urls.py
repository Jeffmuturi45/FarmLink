from django.urls import path
from . import views

app_name = 'produce'

urlpatterns = [
    path('',                        views.produce_list,       name='list'),
    path('post/',                   views.post_produce,       name='post'),
    path('delete/<int:pk>/',        views.delete_produce,     name='delete'),
    path('toggle/<int:pk>/',        views.toggle_availability, name='toggle'),
]
