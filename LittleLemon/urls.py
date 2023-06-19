from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

booking_router = DefaultRouter()
booking_router.register(r"tables", BookingViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('restaurant/menu/', include('restaurant.urls')),
   path('restaurant/booking/', include(booking_router.urls)),
]