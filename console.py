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

instructional_event1 = InstructionalEvent("Yoga", datetime(2021, 11, 17, 18), 90, gender="Female")
instructional_event_repository.save(instructional_event1)
instructional_event2 = InstructionalEvent("Martial Arts", datetime(2021, 11, 20, 19), 60, [member1, member2], 5, 60)
instructional_event_repository.save(instructional_event2)
instructional_event3 = InstructionalEvent("Martial Arts", datetime(2021, 11, 18, 10), 60, [member1, member2], 2, 40)
instructional_event_repository.save(instructional_event3)

instructional_event_repository.add_member(instructional_event1, member1)

instructional_event1.capacity = 10
instructional_event1.duration = 45
instructional_event_repository.update(instructional_event1)

instructional_events = instructional_event_repository.select_all_upcoming()
for instructional_event in instructional_events:
    print(instructional_event.__dict__)

instructional_event3.gender = "Non-binary"
instructional_event_repository.update(instructional_event3)

instructional_event = instructional_event_repository.select(3)
print('\n', instructional_event.__dict__)
