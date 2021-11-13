from flask import Blueprint, render_template
from repositories import instructional_event_repository

classes_blueprint = Blueprint('classes', __name__)

@classes_blueprint.route('/classes')
def show_all():
    instructional_events = instructional_event_repository.select_all_upcoming()
    return render_template("classes/show_all_upcoming.html", instructional_events=instructional_events)

@classes_blueprint.route('/classes/<id>')
def show(id):
    instructional_event = instructional_event_repository.select(id)
    return render_template("classes/show.html", instructional_event=instructional_event)