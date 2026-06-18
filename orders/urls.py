from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('place/<int:produce_pk>/',
         views.place_order,          name='place'),
    path('update/<int:pk>/<str:action>/',
         views.update_order_status,  name='update_status'),
]
