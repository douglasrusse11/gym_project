import unittest
from models.instructional_event import InstructionalEvent
from models.member import Member
from datetime import datetime, date

class TestInstructionalEvent(unittest.TestCase):
    def setUp(self):
        self.instructional_event1 = InstructionalEvent("Yoga", datetime(2021, 11, 12, 18), 90)
        self.member = Member("Augusta", "Eldrick", date(1997, 5, 19), "crobles@yahoo.ca")
        self.instructional_event2 = InstructionalEvent("Martial Arts", datetime(2021, 11, 12, 19), 60, [self.member], 1)

    def test_instructional_event1_has_name(self):
        self.assertEqual("Yoga", self.instructional_event1.name)

    def test_instructional_event1_has_time(self):
        self.assertEqual(datetime(2021, 11, 12, 18), self.instructional_event1.time)

    def test_instructional_event1_has_duration(self):
        self.assertEqual(90, self.instructional_event1.duration)

    def test_instructional_event1_members_is_empty_list(self):
        self.assertEqual([], self.instructional_event1.members)

    def test_instructional_event1_id_is_None(self):
        self.assertIsNone(self.instructional_event1.id)

    def test_instructional_event2_has_members(self):
        self.assertGreater(len(self.instructional_event2.members), 0)

    def test_instructional_event2_has_id(self):
        self.assertEqual(1, self.instructional_event2.id)

    @unittest.skip('')
    def test_end_time(self):
        self.assertEqual(datetime(2021, 11, 12, 19, 30), self.instructional_event1.end_time())
        self.assertEqual(datetime(2021, 11, 12, 20), self.instructional_event2.end_time())
