from flask import Blueprint

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def show_all():
    return "Members go here"

@members_blueprint.route('/members/new')
def add_member():
    return "Add member here"