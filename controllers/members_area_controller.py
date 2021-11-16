from flask import Blueprint, render_template, request, redirect
from repositories import member_repository, instructional_event_repository
from datetime import date

members_area_blueprint = Blueprint('members_area', __name__)

@members_area_blueprint.route('/members_area')
def index():
    return "Members area goes here"

@members_area_blueprint.route('/members_area/<id>')
def show(id):
    member = member_repository.select(id)
    return render_template("members_area/show.html", member=member)

@members_area_blueprint.route('/members_area/<id>', methods=["POST"])
def update_member(id):
    member = member_repository.select(id)
    member.first_name = request.form["first-name"]
    member.last_name = request.form["last-name"]
    year, month, day = (int(element) for element in request.form["dob"].split('-'))
    member.dob = date(year, month, day)
    member.email = request.form["email"]
    member.gender = None if request.form["gender"] == "" else request.form["gender"]
    member_repository.update(member)
    return redirect(f'/members_area/{id}')

@members_area_blueprint.route('/members_area/<id>/edit')
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members_area/edit.html", member=member)

@members_area_blueprint.route('/members_area/<id>/classes')
def show_eligible_classes(id):
    member = member_repository.select(id)
    instructional_events = instructional_event_repository.select_all_upcoming()
    return render_template("members_area/show_all_classes.html", member=member, instructional_events=instructional_events)

@members_area_blueprint.route('/members_area/<member_id>/classes/<instructional_event_id>')
def show_class(member_id, instructional_event_id):
    member = member_repository.select(member_id)
    instructional_event = instructional_event_repository.select(instructional_event_id)
    spaces_remaining = instructional_event.capacity - len(instructional_event.members)
    return render_template("members_area/show_class.html", member=member, instructional_event=instructional_event, spaces_remaining=spaces_remaining)