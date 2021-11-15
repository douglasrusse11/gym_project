from datetime import date

class Member:
    def __init__(self, first_name, last_name, dob, email, gender=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.gender = gender
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return self.id == other.id

    def age(self):
        today = date.today()
        if self.dob.month < today.month:
            return today.year - self.dob.year
        elif self.dob.month == today.month and self.dob.day <= today.day:
            return today.year - self.dob.year
        return today.year - self.dob.year - 1