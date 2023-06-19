from django.db import models

# Create your models here.
#Menu Model
class Menu(models.Model):
  title = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=7, decimal_places=2)
  inventory = models.SmallIntegerField()
  
  def __str__(self):
      return f'{self.title} : {str(self.price)}'
  
  
#Booking Model  
class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.SmallIntegerField()
  booking_date = models.DateTimeField()
  
  def __str__(self):
      return self.name
