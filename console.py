from models.instructional_event import InstructionalEvent
from models.member import Member
from repositories import instructional_event_repository, member_repository
from datetime import datetime, date
import os

os.system('psql -d gym -f db/gym.sql')

member1 = Member("Augusta", "Eldrick", date(1997, 5, 19), "crobles@yahoo.ca")
member_repository.save(member1)
member2 = Member("Rashad", "Yewande", date(1972, 8, 4), "nogin@icloud.com", "Male")
member_repository.save(member2)

instructional_event1 = InstructionalEvent("Yoga", datetime(2021, 11, 12, 18), 90)
instructional_event_repository.save(instructional_event1)
instructional_event2 = InstructionalEvent("Martial Arts", datetime(2021, 11, 12, 19), 60, [member1, member2], 1)
instructional_event_repository.save(instructional_event2)

instructional_event_repository.add_member(instructional_event1, member1)

members = instructional_event_repository.members(instructional_event2)
for member in members:
    print(member.__dict__)