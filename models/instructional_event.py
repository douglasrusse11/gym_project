from datetime import timedelta

class InstructionalEvent:
    def __init__(self, name, time, duration, members=[], capacity=None, id=None):
        self.name = name
        self.time = time
        self.duration = duration
        self.members = members
        self.capacity = capacity
        self.id = id

    def end_time(self):
        return self.time + timedelta(minutes=self.duration)