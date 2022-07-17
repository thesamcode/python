
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

# from flask_app.controllers import controller_user
# from flask_app import app

from flask_app.models.model_user import User

@app.route('/')
def hello_world():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", all_users=all_users)


            
if __name__ == "__main__":
    app.run(debug=True)