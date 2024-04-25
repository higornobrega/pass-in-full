from django.test import TestCase
from django.urls import resolve, reverse

from Attendee import views


class AttendeeViewTest(TestCase):
    def test_attendee_create_attendee_view_function_is_correct(self):
        view = resolve(reverse('attendee:create_attendee'))
        self.assertIs(view.func, views.create_attendee)
    
    def test_attendee_list_attendee_view_function_is_correct(self):
        view = resolve(reverse('attendee:list_attendee'))
        self.assertIs(view.func, views.list_attendee)
    
    def test_attendee_update_attendee_view_function_is_correct(self):
        view = resolve(reverse('attendee:update_attendee', kwargs={'pk': 1}))
        self.assertIs(view.func, views.update_attendee)
    
    def test_attendee_delete_attendee_view_function_is_correct(self):
        view = resolve(reverse('attendee:delete_attendee', kwargs={'pk': 1}))
        self.assertIs(view.func, views.delete_attendee)
        
    def test_attendee_create_attendee_view_returns_code_200(self):
        response = self.client.get(reverse('attendee:create_attendee'))
        self.assertEqual(response.status_code, 200)
        
    def test_attendee_list_attendee_view_returns_status_code_200(self):
        response = self.client.get(reverse('attendee:list_attendee'))
        self.assertEqual(response.status_code,200)
        
    def test_attendee_update_attendee_view_returns_status_code_200(self):
        response = self.client.get(reverse('attendee:update_attendee', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        
    def test_attendee_delete_attendee_view_returns_status_code_200(self):
        response = self.client.get(reverse('attendee:delete_attendee', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        
    def test_attendee_create_attendee_view_loads_correct_template(self):
        response = self.client.get(reverse('attendee:create_attendee'))
        self.assertTemplateUsed(response, 'attendee/create_attendee.html')
        
    def test_attendee_list_attendee_view_loads_correct_template(self):
        response = self.client.get(reverse('attendee:list_attendee'))
        self.assertTemplateUsed(response, 'attendee/list_attendee.html')
        
    def test_attendee_update_attendee_view_loads_correct_template(self):
        response = self.client.get(reverse('attendee:update_attendee', kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'attendee/update_attendee.html')
    
    def test_attendee_delete_attendee_view_loads_correct_template(self):
        response = self.client.get(reverse('attendee:delete_attendee', kwargs={'pk': 1}))
        self.assertTemplateUsed(response,'attendee/list_attendee.html' )
    
    