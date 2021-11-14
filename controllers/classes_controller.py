from flask import Blueprint, render_template, request, redirect
from repositories import instructional_event_repository
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

@classes_blueprint.route('/classes/new')
def add_class():
    return render_template("/classes/new.html")