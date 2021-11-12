class Member:
    def __init__(self, first_name, last_name, dob, email, gender=None, e=None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.gender = gender
        self.id = None