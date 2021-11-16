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
    print(request.form)
    name = request.form["name"]
    time = datetime.strptime(request.form["time"], '%Y-%m-%dT%H:%M')
    duration = request.form["duration"]
    capacity = int(request.form["capacity"])
    min_age = None if request.form["min_age"] == '' else int(request.form["min_age"])
    gender = None if request.form["gender"] == '' else request.form["gender"]
    instructional_event = InstructionalEvent(name, time, duration, capacity=capacity, min_age=min_age, gender=gender)
    instructional_event_repository.save(instructional_event)
    return redirect('/classes')

@classes_blueprint.route('/classes/<id>')
def show(id):
    instructional_event = instructional_event_repository.select(id)
    spaces_remaining = instructional_event.capacity - len(instructional_event.members)
    return render_template("classes/show.html", instructional_event=instructional_event, spaces_remaining=spaces_remaining)

@classes_blueprint.route('/classes/<id>', methods=["POST"])
def update_class(id):
    instructional_event = instructional_event_repository.select(id)
    instructional_event.name = request.form["name"]
    instructional_event.time = datetime.strptime(request.form["time"], '%Y-%m-%dT%H:%M')
    instructional_event.duration = request.form["duration"]
    instructional_event.capacity = int(request.form["capacity"])
    instructional_event.min_age = None if request.form["min_age"] == '' else int(request.form["min_age"])
    instructional_event.gender = None if request.form["gender"] == '' else request.form["gender"]
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
    eligible_members = instructional_event_repository.eligible_members(instructional_event)
    spaces_remaining = instructional_event.capacity - len(instructional_event.members)
    return render_template("classes/book.html", instructional_event=instructional_event, members=eligible_members, spaces_remaining=spaces_remaining)

@classes_blueprint.route('/classes/<id>/book', methods=["POST"])
def add_member_to_class(id):
    instructional_event = instructional_event_repository.select(id)
    member = member_repository.select(request.form["member_id"])
    instructional_event_repository.add_member(instructional_event, member)
    return redirect(f"/classes/{instructional_event.id}")