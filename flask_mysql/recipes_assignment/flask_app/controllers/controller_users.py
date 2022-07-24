
from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe
from flask_app.models import model_user

@app.route('/')
def homepage():
    if 'uuid' in session:
        return redirect('/recipes')
    return render_template("index.html")

@app.route('/user/create_user', methods=['POST'])
def create_user():
    # validations
    if not model_user.User.validate_user(request.form):
        return redirect('/')
    
    # hashing
    hash_password = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hash_password
    }

    # create my user
    id = model_user.User.create_user(data)

    # store user_id in session
    session['uuid'] = id
    return redirect('/recipes')    
    
    
    # User.save(request.form)
    # return redirect('/recipes')


    # print(request.form)
    # is_valid = User.validate_user(request.form)
    # if not is_valid:
    #     return redirect('/')
    # data = {
    #     "first_name":request.form['first_name'],
    #     "last_name":request.form['last_name']
    # }

@app.route('/recipes')
def all_recipes():
    if 'uuid' not in session:
        return redirect('/')
    # data = {
    #     "id":id
    # }
    #the below variable can be recipes or all_recipes, only being calle din html...
    return render_template("all_recipes.html", all_recipes=Recipe.get_recipe_with_users())

@app.route('/user/login', methods=['POST'])
def login_user():
    # validate
    if not model_user.User.validate_login(request.form):
        return redirect('/')
    # session['uuid'] = model_user.User.get_one_by_email({'email':request.form['email']}).id

    return redirect('/recipes')

@app.route('/user/logout')
def logout_user():
    #using clear session would delete the remeber me function as well... So we use this one
    del session['uuid']
    return redirect('/')