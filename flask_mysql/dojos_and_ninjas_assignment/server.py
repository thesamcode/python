

from flask_app import app
# from users import User

from flask_app.controllers import controller_dojos, controller_ninjas

# app=Flask(__name__)



if __name__=="__main__":
    app.run(debug=True)
