from flask import Blueprint, render_template, request, redirect
from repositories import member_repository
from models.member import Member
from datetime import date, datetime, timedelta

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def show_all():
    members = member_repository.select_all()
    return render_template("members/show_all.html", members=members)

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
    return redirect('/members')

@members_blueprint.route('/members/new')
def add_member():
    max_dob = date.today() - timedelta(hours=18*365.25*24)
    return render_template("members/new.html", max_dob=max_dob)

@members_blueprint.route('/members/<id>', methods=["POST"])
def update_member(id):
    member = member_repository.select(id)
    member.first_name = request.form["first-name"]
    member.last_name = request.form["last-name"]
    year, month, day = (int(element) for element in request.form["dob"].split('-'))
    member.dob = date(year, month, day)
    member.email = request.form["email"]
    member.gender = None if request.form["gender"] == "" else request.form["gender"]
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route('/members/<id>/edit')
def edit_member(id):
    member = member_repository.select(id)
    max_dob = date.today() - timedelta(hours=18*365.25*24)
    return render_template("members/edit.html", member=member, max_dob=max_dob)