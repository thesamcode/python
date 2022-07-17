
# from flask import Flask, render_template, redirect, request, session
# app = Flask(__name__)

from flask_app import app
from flask_app.controllers import controller_user, controller_event

# from flask_app.controllers import controller_user
# from flask_app import app

# THIS WILL MOVE IN FUTURE



# END OF MOVING AREA
# # THIS MUST BE ON BOTTOM OF FILE            
if __name__ == "__main__":
    app.run(debug=True)