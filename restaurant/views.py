from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

#MenuItemView
class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


#SingleMenuItemView
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#BookingView
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    