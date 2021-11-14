from flask import Blueprint, render_template, request, redirect
from repositories import member_repository
from models.member import Member
from datetime import date

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def show_all():
    return "Members go here"

@members_blueprint.route('/members', methods=["POST"])
def save_member():
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    year, month, day = (int(element) for element in request.form["dob"].split('-'))
    dob = date(year, month, day)
    email = request.form["email"]
    gender = None if request.form["gender"] == "" else request.form["gender"]
    member = Member(first_name, last_name, dob, email, gender)
    member_repository.save(member)
    return "Member added"

@members_blueprint.route('/members/new')
def add_member():
    return render_template("members/new.html")

@members_blueprint.route('/members/<id>/edit')
def edit_member(id):
    member = member_repository.select(id)
    return f"Edit Member: {member.__dict__}"