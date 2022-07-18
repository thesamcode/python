
# from flask import Flask, render_template, redirect, request, session
# app = Flask(__name__)


from flask_app import app
from flask_app.controllers import controller_users






if __name__ == "__main__":
    app.run(debug=True)