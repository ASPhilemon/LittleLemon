from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView


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
