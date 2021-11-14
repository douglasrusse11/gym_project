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