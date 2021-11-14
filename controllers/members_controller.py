from flask import Blueprint, render_template, request

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def show_all():
    return "Members go here"

@members_blueprint.route('/members', methods=["POST"])
def save_member():
    print(request.form)
    return "Member added"

@members_blueprint.route('/members/new')
def add_member():
    return render_template("members/new.html")