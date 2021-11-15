from flask import Blueprint, render_template
from repositories import member_repository

members_area_blueprint = Blueprint('members_area', __name__)

@members_area_blueprint.route('/members_area')
def index():
    return "Members area goes here"

@members_area_blueprint.route('/members_area/<id>')
def show(id):
    member = member_repository.select(id)
    return f"Member {member.full_name()}'s profile goes here"