from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class AtetendeeURLTest(TestCase):
    def test_list_attendee_url_is_correct(self):
        url = reverse('attendee:list_attendee')
        self.assertEqual(url, '/attendee/list_attendee/')
        
    def test_create_attendee_url_is_correct(self):
        url = reverse('attendee:create_attendee')
        self.assertEqual(url, '/attendee/create_attendee/')
        
    def test_update_attendee_url_is_correct(self):
        url = reverse('attendee:update_attendee', args=[1])
        self.assertEqual(url, '/attendee/update_attendee/1/')
        
    def test_delete_attendee_url_is_correct(self):
        url = reverse('attendee:delete_attendee', args=[1])
        self.assertEqual(url, '/attendee/delete_attendee/1/')