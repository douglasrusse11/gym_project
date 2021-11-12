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