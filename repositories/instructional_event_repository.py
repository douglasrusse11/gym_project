from db.run_sql import run_sql
from models.instructional_event import InstructionalEvent
from repositories import member_repository

def save(instructional_event):
    sql = """INSERT INTO instructional_events (name, time, duration)
             VALUES (%(name)s, %(time)s, %(duration)s) 
             RETURNING *
             """
    values = {
              'name': instructional_event.name,
              'time': instructional_event.time,
              'duration': instructional_event.duration
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
