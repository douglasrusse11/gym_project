from db.run_sql import run_sql
from models.instructional_event import InstructionalEvent

def save(instructional_event):
    sql = """INSERT INTO instructional_events (name, time, duration)
             VALUES (%(name)s, %(time)s, %(duration)s) 
             RETURNING *
             """
    values = {'name': instructional_event.name,
              'time': instructional_event.time,
              'duration': instructional_event.duration
              }
    result = run_sql(sql, values)[0]
    instructional_event.id = result["id"]
