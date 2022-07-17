

from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.model_user import User

# Display
@app.route('/')
def hello_world():
    all_users = User.get_all()
    # print(all_users)
    return render_template("index.html", all_users=all_users)

# Action
@app.route('/user/create', methods=['POST'])
def user_create():
    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')

    # Hashing the pw using bcrypt
    hash_pw = bcrypt.generate_password_hash(request.form['pw'], 13)
    # print(hash_pw)
    # data = {
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'numandstreet': request.form['numandstreet'],
    #     'city': request.form['city'],
    #     'state': request.form['state'],
    #     'zip': request.form['zip'],
    #     'pw': hash_pw,
    # }
    data = {
        **request.form,
        'pw':hash_pw
    }


    # user_id = User.create(request.form)
    user_id = User.create(data)
    session['user_id'] = user_id
    # print("I made it here")
    # print(request.form)
    return redirect('/')

@app.route('/user/check_password', methods = ['POST'])
def check_password():
    # print(request.form)
    #Get the user by their id
    potential_user = User.get_one({'id': request.form['id']})
    # print(potential_user.fullname)
    # print(potential_user.pw)


    #compare their user id to the hashed version of incoming password
    # is_correct = bcrypt.check_password_hash(potential_user.pw, request.form['pw'])
    # print(is_correct)

    #if good, we say yes and log the user in
    #if not we say no and kick them back to the login


    is_valid = User.validate_login(request.form)

    if not is_valid:
        print("not correct")
        return redirect('/')
    return redirect('/')

# RESTfull
# table_name/id(if possible)/action
# user/new -> DISPLAY ROUTE this is usually registration page
# user/create -> ACTION ROUTE creates a user
# user/<int:is> -> DISPLAY ROUTE
# user/<int:id>/edit -> DISPLAY ROUTE
# user/<int:id>/update -> updates info that they gave us. ACTION ROUTE
# user/<int:is>/delete -> ACTION ROUTE









# from flask import render_template
# from flask_app import app

# @app.route("/")
# def index():
#     # # call the get all classmethod to get all friends
#     # friends = Friend.get_all()
#     # print(friends)
#     return render_template("index.html")


