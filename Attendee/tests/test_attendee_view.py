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