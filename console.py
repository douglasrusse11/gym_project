from models.instructional_event import InstructionalEvent
from models.member import Member
from repositories import instructional_event_repository, member_repository
from datetime import datetime, date
from random import randint, choice
import os

os.system('psql -d gym -f db/gym.sql')

member1 = Member("Aga", "Koltun", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "aga@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member1)
member2 = Member("Almas", "Butt", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "almas@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member2)
member3 = Member("Andrew", "Calder", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "andrew@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member3)
member4 = Member("David", "McIntyre", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "david@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member4)
member5 = Member("Douglas", "Russell", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "douglas@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member5)
member6 = Member("Gavin", "Hargin", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "gavin@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member6)
member7 = Member("Graeme", "Brown", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "graeme@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member7)
member8 = Member("Louis", "Fletcher", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "louis@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member8)
member9 = Member("Martin", "Quinn", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "martin@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member9)
member10 = Member("Michael", "Plata", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "michael@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member10)
member11 = Member("Nicole", "Sneddon", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "nicole@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member11)
member12 = Member("Roger", "Malgueira", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "roger@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member12)
member13 = Member("Stefano", "Binando", date(randint(1940, 2000), randint(1, 12), randint(1,28)), "stefano@gym.com", choice(["Male", "Female", "Non-binary", None]))
member_repository.save(member13)


instructional_event1 = InstructionalEvent("Yoga", datetime(2021, 11, 17, 18), 90, 1)
instructional_event_repository.save(instructional_event1)
instructional_event2 = InstructionalEvent("Martial Arts", datetime(2021, 11, 20, 19), 120, 10)
instructional_event_repository.save(instructional_event2)
instructional_event3 = InstructionalEvent("Swimming", datetime(2021, 11, 18, 10), 60, 20, gender="Female")
instructional_event_repository.save(instructional_event3)
instructional_event4 = InstructionalEvent("Aquarobics", datetime(2021, 11, 18, 10), 60, 15, min_age=60)
instructional_event_repository.save(instructional_event4)