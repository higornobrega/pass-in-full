from django.test import TestCase

from Attendee.models import Attendee


class AttendeeTestBase(TestCase):
    def setUp(self) -> None:
        attendee = Attendee.objects.create(name='Higor Stefany dos Santos Nóbrega', email='higorst.nobrega@gmail.com')
        return super().setUp()
