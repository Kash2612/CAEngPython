from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('api/', include('base.urls')),  # Include base app URLs
    path('auth/', include('rest_framework.urls')),  # Include authentication URLs from DRF
]
