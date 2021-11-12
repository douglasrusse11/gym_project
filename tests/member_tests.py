import unittest
from models.member import Member
from datetime import date

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member1 = Member("Augusta", "Eldrick", date(1997, 5, 19), "crobles@yahoo.ca")
        self.member2 = Member("Rashad", "Yewande", date(1972, 8, 4), "nogin@icloud.com", "Male", 1)

    def test_member1_has_first_name(self):
        self.assertEqual("Augusta", self.member1.first_name)

    def test_member1_has_last_name(self):
        self.assertEqual("Eldrick", self.member1.last_name)

    def test_member1_has_dob(self):
        self.assertEqual(date(1997, 5, 19), self.member1.dob)

    def test_member1_has_email(self):
        self.assertEqual("crobles@yahoo.ca", self.member1.email)

    def test_member1_gender_is_None(self):
        self.assertIsNone(self.member1.gender)

    def test_member1_id_is_None(self):
        self.assertIsNone(self.member1.id)

    @unittest.skip('')
    def test_member2_has_gender(self):
        self.assertEqual("Male", self.member2.gender)

    @unittest.skip('')
    def test_member2_has_id(self):
        self.assertEqual(1, self.member2.id)

    @unittest.skip('')
    def test_full_name(self):
        self.assertEqual("Augusta Eldrick", self.member1.full_name())
        self.assertEqual("Rashad Yewande", self.member2.full_name())
