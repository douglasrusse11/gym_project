from db.run_sql import run_sql
from models.instructional_event import InstructionalEvent
from repositories import member_repository
from datetime import datetime

def save(instructional_event):
    sql = """INSERT INTO instructional_events (name, time, duration, capacity)
             VALUES (%(name)s, %(time)s, %(duration)s, %(capacity)s) 
             RETURNING *"""
    values = {
              'name': instructional_event.name,
              'time': instructional_event.time,
              'duration': instructional_event.duration,
              'capacity': instructional_event.capacity
              }
    result = run_sql(sql, values)[0]
    instructional_event.id = result["id"]
    if instructional_event.members is not []:
        for member in instructional_event.members:
            add_member(instructional_event, member)

def add_member(instructional_event, member):
    sql = """INSERT INTO gym (member_id, instructional_event_id)
             VALUES (%(member_id)s, %(instructional_event_id)s)"""
    values = {
              'member_id': member.id,
              'instructional_event_id': instructional_event.id
              }
    run_sql(sql, values)

def members(instructional_event):
    members = []
    sql = """SELECT members.id FROM members
             INNER JOIN gym ON members.id = gym.member_id
             INNER JOIN instructional_events
             ON gym.instructional_event_id = instructional_events.id
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
            instructional_event = InstructionalEvent(result["name"], result["time"], result["duration"], capacity= result["capacity"], id=result["id"])
            instructional_event.members = members(instructional_event)
            instructional_events.append(instructional_event)
    instructional_events.sort(key=sort_by_time_key)
    return instructional_events

def remove_members(instructional_event):
    sql = "DELETE FROM gym WHERE instructional_event_id = %s"
    values = [instructional_event.id]
    run_sql(sql, values)

def update(instructional_event):
    sql = """UPDATE instructional_events SET (name, time, duration, capacity)
             = (%(name)s, %(time)s, %(duration)s, %(capacity)s) WHERE id = %(id)s"""
    values = {
              'name': instructional_event.name,
              'time': instructional_event.time,
              'duration': instructional_event.duration,
              'capacity': instructional_event.capacity,
              'id': instructional_event.id
              }
    run_sql(sql, values)
    remove_members(instructional_event)
    for member in instructional_event.members:
        add_member(instructional_event, member)

def sort_by_time_key(instructional_event):
    return instructional_event.time

def select(id):
    instructional_event = None
    sql = "SELECT * FROM instructional_events WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        instructional_event = InstructionalEvent(result["name"], result["time"], result["duration"], capacity=result["capacity"], id=result["id"])
        instructional_event.members = members(instructional_event)
    return instructional_event