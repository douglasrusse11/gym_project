from flask import Blueprint

members_blueprint = Blueprint('members', __name__)

@members_blueprint.route('/members')
def show_all():
    return "Members go here"