from django.test import TestCase

from Attendee.models import Attendee


class AttendeeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_attendee(self, name = 'Higor Stefany dos Santos Nóbrega', email='higorst.nobrega@gmail.com'):
        return Attendee.objects.create(name=name, email=email)
        