from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestClass(TestCase):
    
    def setUp(self):
        """
        create a location
        """
        Location.objects.create(locationx = 'Rongai')
        self.location = Location.objects.get(locationx = "Rongai")

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_update_location(self):
        self.location.update_location(Kenya)
        locationx = Location.objects.all()
        self.assertEqual(locationx.locationx, 'Kenya')