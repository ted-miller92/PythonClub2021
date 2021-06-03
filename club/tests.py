from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(title="Test Meeting")
        self.assertEqual(str(type), type.title)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setup(self):
        meeting=Meeting(title="Test Meeting")
        return meeting.title
    def test_string(self):
        meetingId=self.setup()
        self.assertEqual(str(meetingId), meetingId)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingMinutes')

class ResourceTest(TestCase):
    def test_string(self):
        resource= Resource(resourceName="Django Documentation")
        self.assertEqual(str(resource), resource.resourceName)
    
    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        event=Event(eventTitle="Test Event")
        self.assertEqual(str(event), event.eventTitle)
    
    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')