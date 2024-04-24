from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class AtetendeeURLTest(TestCase):
    def test_list_attendee_url_is_correct(self):
        reverse_url = reverse('attendee:list_attendee')
        print('reverse_url')
        print(reverse_url)
        self.assertEqual(reverse_url, '/attendee/list_attendee/')