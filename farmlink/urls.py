from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


def landing(request):
    # Sample produce cards for the landing page preview
    sample_produce = [
        {'emoji': '🌽', 'name': 'Maize', 'farmer': 'John Kamau',
            'location': 'Nakuru', 'price': '4,200', 'qty': '90kg bag'},
        {'emoji': '🍅', 'name': 'Tomatoes', 'farmer': 'Mary Wanjiku',
            'location': 'Nyeri', 'price': '1,800', 'qty': 'Per crate'},
        {'emoji': '🥔', 'name': 'Potatoes', 'farmer': 'Peter Mwangi',
            'location': 'Nyandarua', 'price': '3,500', 'qty': '50kg bag'},
        {'emoji': '🥑', 'name': 'Avocado', 'farmer': 'Grace Akinyi',
            'location': 'Kisii', 'price': '5,000', 'qty': 'Per crate'},
    ]
    return render(request, 'landing.html', {'sample_produce': sample_produce})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('produce/', include('produce.urls')),
    path('orders/', include('orders.urls')),
    path('admin-panel/', include('admin_dashboard.urls')),
    path('notifications/', include('notifications.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
