import unittest
from models.member import Member
from datetime import date

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member1 = Member("Augusta", "Eldrick", date(1997, 5, 19), "crobles@yahoo.ca")
        self.member2 = Member("Rashad", "Yewande", date(1972, 8, 4), "nogin@icloud.com", "Male", 1)
        self.member3 = Member("Augusta", "Eldrick", date(1997, 5, 19), "crobles@yahoo.ca")
        self.member4 = Member("Augusta", "Eldrick", date(1997, 11, 14), "crobles@yahoo.ca")
        self.member5 = Member("Augusta", "Eldrick", date(1997, 11, 15), "crobles@yahoo.ca")
        self.member6 = Member("Augusta", "Eldrick", date(1997, 11, 16), "crobles@yahoo.ca")
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

    def test_member2_has_gender(self):
        self.assertEqual("Male", self.member2.gender)

    def test_member2_has_id(self):
        self.assertEqual(1, self.member2.id)

    def test_full_name(self):
        self.assertEqual("Augusta Eldrick", self.member1.full_name())
        self.assertEqual("Rashad Yewande", self.member2.full_name())

    def test_member_equality(self):
        self.assertEqual(self.member1, self.member3)

    def test_member1_age(self):
        self.assertEqual(24, self.member1.age())

    def test_member2_age(self):
        self.assertEqual(49, self.member2.age())

    def test_member4_age(self):
        self.assertEqual(24, self.member4.age())

    def test_member5_age(self):
        self.assertEqual(24, self.member5.age())

    def test_member6_age(self):
        self.assertEqual(23, self.member6.age())