from flask import Flask, render_template, request
from controllers.classes_controller import classes_blueprint
from controllers.members_controller import members_blueprint
from controllers.members_area_controller import members_area_blueprint

app = Flask(__name__)
app.register_blueprint(classes_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(members_area_blueprint)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def handle_login_request():
    print(request.form)
    return "Log in successful"

if __name__ == '__main__':
    app.run(debug=True)