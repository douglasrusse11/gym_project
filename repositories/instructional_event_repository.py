from db.run_sql import run_sql
from models.instructional_event import InstructionalEvent
from repositories import member_repository
from datetime import datetime, date

def save(instructional_event):
    sql = """INSERT INTO instructional_events (name, time, duration, capacity, min_age, gender)
             VALUES (%(name)s, %(time)s, %(duration)s, %(capacity)s, %(min_age)s, %(gender)s) 
             RETURNING *"""
    values = {
              'name': instructional_event.name,
              'time': instructional_event.time,
              'duration': instructional_event.duration,
              'capacity': instructional_event.capacity,
              'min_age': instructional_event.min_age,
              'gender': instructional_event.gender
              }
    result = run_sql(sql, values)[0]
    instructional_event.id = result["id"]
    if instructional_event.members is not []:
        for member in instructional_event.members:
            add_member(instructional_event, member)

def add_member(instructional_event, member):
    sql = """INSERT INTO bookings (member_id, instructional_event_id)
             VALUES (%(member_id)s, %(instructional_event_id)s)"""
    values = {
              'member_id': member.id,
              'instructional_event_id': instructional_event.id
              }
    run_sql(sql, values)

def members(instructional_event):
    members = []
    sql = """SELECT members.id FROM members
             INNER JOIN bookings ON members.id = bookings.member_id
             INNER JOIN instructional_events
             ON bookings.instructional_event_id = instructional_events.id
             WHERE instructional_events.id = %s"""
    values = [instructional_event.id]
    results = run_sql(sql, values)
    if results is not None:
        for result in results:
            member = member_repository.select(result["id"])
            members.append(member)
    return members

def select_all_upcoming():
    instructional_events = []
    sql = "SELECT * FROM instructional_events WHERE time > %s"
    values = [datetime.now()]
    results = run_sql(sql, values)
    if results is not None:
        for result in results:
            instructional_event = InstructionalEvent(result["name"], result["time"], result["duration"], capacity=result["capacity"], min_age=result["min_age"], gender=result["gender"], id=result["id"])
            instructional_event.members = members(instructional_event)
            instructional_events.append(instructional_event)
    instructional_events.sort(key=sort_by_time_key)
    return instructional_events

def update(instructional_event):
    sql = """UPDATE instructional_events SET (name, time, duration, capacity, min_age, gender)
             = (%(name)s, %(time)s, %(duration)s, %(capacity)s, %(min_age)s, %(gender)s) WHERE id = %(id)s"""
    values = {
              'name': instructional_event.name,
              'time': instructional_event.time,
              'duration': instructional_event.duration,
              'capacity': instructional_event.capacity,
              'min_age': instructional_event.min_age,
              'gender': instructional_event.gender,
              'id': instructional_event.id
              }
    run_sql(sql, values)

def sort_by_time_key(instructional_event):
    return instructional_event.time

def select(id):
    instructional_event = None
    sql = "SELECT * FROM instructional_events WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        instructional_event = InstructionalEvent(result["name"], result["time"], result["duration"], capacity=result["capacity"], min_age=result['min_age'], gender=result["gender"], id=result["id"])
        instructional_event.members = members(instructional_event)
    return instructional_event

def eligible_members(instructional_event):
    members = []
    if instructional_event.has_capacity():
        sql = "SELECT * FROM members WHERE id NOT IN %(members_id_list)s"
        values = {'members_id_list': (-1, ) if instructional_event.members == [] else tuple([member.id for member in instructional_event.members])}
        if instructional_event.min_age:
            today = date.today()
            max_dob = today.replace(year=today.year-instructional_event.min_age)
            sql += " AND members.dob < %(max_dob)s"
            values["max_dob"] = max_dob
        if instructional_event.gender:
            sql += " AND gender = %(instructional_event_gender)s"
            values["instructional_event_gender"] = instructional_event.gender
        results = run_sql(sql, values)
        if results is not None:
            for result in results:
                member = member_repository.select(result["id"])
                members.append(member)
    return members