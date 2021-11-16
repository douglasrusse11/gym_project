from flask import Flask, render_template, request, redirect
from controllers.classes_controller import classes_blueprint
from controllers.members_controller import members_blueprint
from controllers.members_area_controller import members_area_blueprint
from repositories import member_repository

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
    username = request.form["username"]
    if username == "staff":
        return redirect('/classes')
    member = member_repository.select_by_name(username)
    if member:
        return redirect(f"/members_area/{member.id}")
    else:
        return redirect("/login")

@app.route('/attribution')
def attribution():
    return render_template("attribution.html")

if __name__ == '__main__':
    app.run(debug=True)