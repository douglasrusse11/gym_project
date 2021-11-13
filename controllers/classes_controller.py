from flask import Blueprint
from repositories import instructional_event_repository

classes_blueprint = Blueprint('classes', __name__)

@classes_blueprint.route('/classes')
def show_all():
    instructional_events = instructional_event_repository.select_all_upcoming()
    return f"{[instructional_event.__dict__ for instructional_event in instructional_events]}"