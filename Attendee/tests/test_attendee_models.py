from django.core.exceptions import ValidationError

from .test_attendee_base import AttendeeTestBase


class AttendeeModelTest(AttendeeTestBase):
    def setUp(self) -> None:
        self.attendee = self.make_attendee()
        return super().setUp()
    
    def test_attendee_name_raises_error_if_name_has_more_than_65_chars(self):
        self.attendee.name = "A"*256
        
        with self.assertRaises(ValidationError):
            self.attendee.full_clean()    
            
    def test_attendee_string_representation(self):
        self.attendee.name = 'Higor Nóbrega'
        self.attendee.full_clean()
        self.attendee.save()
        self.assertEqual(str(self.attendee), 'Higor Nóbrega') 