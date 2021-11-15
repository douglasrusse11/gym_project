from flask import Blueprint, render_template

members_area_blueprint = Blueprint('members_area', __name__)

@members_area_blueprint.route('/members_area')
def index():
    return "Members area goes here"