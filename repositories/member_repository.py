from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = """INSERT INTO members (first_name, last_name, dob, email, gender)
             VALUES (%(first_name)s, %(last_name)s, %(dob)s, %(email)s, %(gender)s)
             RETURNING *"""
    values = {'first_name': member.first_name, 
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
        member = Member(result['first_name'], result['last_name'], result['dob'], result['email'], result['gender'], id)
    return member

