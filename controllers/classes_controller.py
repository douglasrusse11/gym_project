from flask import Blueprint

classes_blueprint = Blueprint('classes', __name__)

@classes_blueprint.route('/classes')
def show_all():
    return "Classes go here"