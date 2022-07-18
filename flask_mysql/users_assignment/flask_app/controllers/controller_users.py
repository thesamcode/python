

from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.model_user import User

app.route('/')
def index():
    return redirect('/users')

app.route('/users')
def hello_world():
    all_users = User.get_all()
    return render_template("users.html", all_users=all_users)

app.route('/users/new')
def new():
    return render_template("new.html")

@app.route('/users/create', methods=['POST'])
def user_create():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/users')    