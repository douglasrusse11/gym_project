from db.run_sql import run_sql
from models.member import Member
from repositories import instructional_event_repository
from datetime import datetime

def save(member):
    sql = """INSERT INTO members (first_name, last_name, dob, email, gender)
             VALUES (%(first_name)s, %(last_name)s, %(dob)s, %(email)s, %(gender)s)
             RETURNING *"""
    values = {
              'first_name': member.first_name, 
              'last_name': member.last_name,
              'dob': member.dob,
              'email': member.email,
              'gender': member.gender
              }
    result = run_sql(sql, values)[0]
    member.id = result["id"]

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['dob'], result['email'], result['gender'], result['id'])
    return member

def update(member):
    sql = """UPDATE members SET (first_name, last_name, dob, email, gender)
             = (%(first_name)s, %(last_name)s, %(dob)s, %(email)s, %(gender)s)
             WHERE id = %(id)s"""
    values = {
              'first_name': member.first_name, 
              'last_name': member.last_name,
              'dob': member.dob,
              'email': member.email,
              'gender': member.gender,
              'id': member.id
              }
    run_sql(sql, values)

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        first_name = result["first_name"]
        last_name = result["last_name"]
        dob = result["dob"]
        email = result["email"]
        gender = result["gender"]
        id = result["id"]
        member = Member(first_name, last_name, dob, email, gender, id)
        members.append(member)
    return members

def select_by_name(full_name):
    member = None
    names = full_name.split()
    if len(names) != 2:
        return member
    sql = """SELECT * FROM members WHERE first_name = %(first_name)s
           AND last_name = %(last_name)s"""
    values = {
              'first_name': names[0],
              'last_name': names[1]
             }
    results = run_sql(sql, values)
    if results != []:
        result = results[0]
        member = Member(result['first_name'], result['last_name'], result['dob'], result['email'], result['gender'], result['id'])
    return member

def eligible_classes(member):
    instructional_events = []
    conditional = False
    sql = """SELECT * FROM instructional_events
             WHERE (gender = %(gender)s OR gender IS NULL)
             AND (min_age < %(age)s OR min_age IS NULL)
             AND time > %(now)s"""
    values = {
              'gender': member.gender,
              'age': member.age(),
              'now': datetime.now()
              }
    results = run_sql(sql, values)
    for result in results:
        instructional_event = instructional_event_repository.select(result["id"])
        instructional_events.append(instructional_event)
    return instructional_events
    
