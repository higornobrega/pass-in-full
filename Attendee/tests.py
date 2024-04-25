from django.test import TestCase
from django.urls import resolve, reverse

from Attendee import views


# Create your tests here.
class AtetendeeURLTest(TestCase):
    def test_create_attendee_url_is_correct(self):
        url = reverse('attendee:create_attendee')
        self.assertEqual(url, '/attendee/create_attendee/')
    
    def test_list_attendee_url_is_correct(self):
        url = reverse('attendee:list_attendee')
        self.assertEqual(url, '/attendee/list_attendee/')    
        
    def test_update_attendee_url_is_correct(self):
        url = reverse('attendee:update_attendee', args=[1]) # kwargs={'pk': 1}
        self.assertEqual(url, '/attendee/update_attendee/1/')
        
    def test_delete_attendee_url_is_correct(self):
        url = reverse('attendee:delete_attendee', args=[1]) # kwargs={'pk': 1}
        self.assertEqual(url, '/attendee/delete_attendee/1/')
        
        
class AttendeeViewTest(TestCase):
    def test_attendee_create_attendee_is_correct(self):
        view = resolve(reverse('attendee:create_attendee'))
        self.assertIs(view.func, views.create_attendee)
    
    def test_attendee_list_attendee_is_correct(self):
        view = resolve(reverse('attendee:list_attendee'))
        self.assertIs(view.func, views.list_attendee)
    
    def test_attendee_update_attendee_is_correct(self):
        view = resolve(reverse('attendee:update_attendee', kwargs={'pk': 1}))
        self.assertIs(view.func, views.update_attendee)
    
    def test_attendee_delete_attendee_is_correct(self):
        view = resolve(reverse('attendee:delete_attendee', kwargs={'pk': 1}))
        self.assertIs(view.func, views.delete_attendee)