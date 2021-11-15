from flask import Blueprint, render_template, request, redirect
from repositories import member_repository
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
    return f"Member {member.full_name()}'s eligible classes go here"