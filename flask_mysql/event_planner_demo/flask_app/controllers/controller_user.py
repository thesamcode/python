

from flask import render_template
from flask_app import app

@app.route("/")
def index():
    # # call the get all classmethod to get all friends
    # friends = Friend.get_all()
    # print(friends)
    return render_template("index.html")