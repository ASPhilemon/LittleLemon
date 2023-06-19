from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

#TestCase class
class MenuViewTest(TestCase):
  
  def setup(self):
    menu_item = Menu.objects.filter(pk = 3)
    return menu_item
  
  
  def test_get_item(self):
    menu_item = self.setup()
    serialized_item = MenuSerializer(menu_item)
    self.assertEqual('2', "2")