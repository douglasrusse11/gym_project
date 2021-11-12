from flask import Flask
from controllers.classes_controller import classes_blueprint
from controllers.members_controller import members_blueprint

app = Flask(__name__)
app.register_blueprint(classes_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)