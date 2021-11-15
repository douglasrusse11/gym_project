from flask import Blueprint, render_template, request, redirect
from repositories import instructional_event_repository, member_repository
from models.instructional_event import InstructionalEvent
from datetime import datetime

classes_blueprint = Blueprint('classes', __name__)

@classes_blueprint.route('/classes')
def show_all():
    instructional_events = instructional_event_repository.select_all_upcoming()
    return render_template("classes/show_all_upcoming.html", instructional_events=instructional_events)

@classes_blueprint.route('/classes', methods=["POST"])
def save_class():
    name = request.form["name"]
    date, time = request.form["time"].split('T')
    year, month, day = (int(element) for element in date.split('-'))
    hour, minute = (int(element) for element in time.split(':'))
    time = datetime(year, month, day, hour, minute)
    duration = request.form["duration"]
    instructional_event = InstructionalEvent(name, time, duration)
    instructional_event_repository.save(instructional_event)
    return redirect('/classes')

@classes_blueprint.route('/classes/<id>')
def show(id):
    instructional_event = instructional_event_repository.select(id)
    return render_template("classes/show.html", instructional_event=instructional_event)

@classes_blueprint.route('/classes/<id>', methods=["POST"])
def update_class(id):
    instructional_event = instructional_event_repository.select(id)
    instructional_event.name = request.form["name"]
    date, time = request.form["time"].split('T')
    year, month, day = (int(element) for element in date.split('-'))
    hour, minute = (int(element) for element in time.split(':'))
    instructional_event.time = datetime(year, month, day, hour, minute)
    instructional_event.duration = request.form["duration"]
    instructional_event_repository.update(instructional_event)
    return redirect(f'/classes/{id}')

@classes_blueprint.route('/classes/new')
def add_class():
    return render_template("/classes/new.html")

@classes_blueprint.route('/classes/<id>/edit')
def edit_class(id):
    instructional_event = instructional_event_repository.select(id)
    return render_template("classes/edit.html", instructional_event=instructional_event)

@classes_blueprint.route('/classes/<id>/book')
def book_class(id):
    instructional_event = instructional_event_repository.select(id)
    if instructional_event.has_capacity():
        members = member_repository.select_all()
        eligible_members = [member for member in members if member not in instructional_event.members]
    else:
        eligible_members = []
    return render_template("classes/book.html", instructional_event=instructional_event, members=eligible_members)

@classes_blueprint.route('/classes/<id>/book', methods=["POST"])
def add_member_to_class(id):
    instructional_event = instructional_event_repository.select(id)
    member = member_repository.select(request.form["member_id"])
    instructional_event.members.append(member)
    instructional_event_repository.update(instructional_event)
    return redirect(f"/classes/{instructional_event.id}")