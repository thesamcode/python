
from flask import Flask, render_template, redirect, request, session
from friend import Friend

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html")
            
if __name__ == "__main__":
    app.run(debug=True)