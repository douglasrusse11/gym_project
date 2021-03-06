from datetime import timedelta

class InstructionalEvent:
    def __init__(self, name, time, duration, capacity, min_age=None, gender=None, id=None):
        self.name = name
        self.time = time
        self.duration = duration
        self.members = []
        self.capacity = capacity
        self.min_age = min_age
        self.gender = gender
        self.id = id

    def end_time(self):
        return self.time + timedelta(minutes=self.duration)

    def has_capacity(self):
        if self.capacity is not None:
            return len(self.members) < self.capacity
        return True