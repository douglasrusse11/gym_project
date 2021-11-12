class InstructionalEvent:
    def __init__(self, name, time, duration, members=[], id=None):
        self.name = name
        self.time = time
        self.duration = duration
        self.members = members
        self.id = id