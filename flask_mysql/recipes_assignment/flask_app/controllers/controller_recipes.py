
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_recipe import Recipe
from flask_app.models import model_recipe
# from flask_app.models.model_user import User

@app.route('/recipes/new')
def new():
    if 'uuid' not in session:
        return redirect('/')
    return render_template("new_recipe.html")

@app.route('/recipes/create_recipe', methods=['POST'])
def create_recipe():
    if 'uuid' not in session:
        return redirect('/')
    if not model_recipe.Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    print(request.form)
    Recipe.save(request.form)
    return redirect('/recipes')
    
    # return redirect('/recipes')
    # hashing

    # create my user

    # store user_id in session


@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'uuid' not in session:
        return redirect('/')
    data = {
        "id":id
    }
    return render_template("edit_recipe.html", recipe=Recipe.get_one(data))

@app.route('/recipes/update',methods=['POST'])
def update_recipe():
    if 'uuid' not in session:
        return redirect('/')
    if not model_recipe.Recipe.validate_recipe(request.form):
        # what below line does it pull data from the html sheet. 
        return redirect(f"/recipes/edit/{request.form['recipe_id']}")
    Recipe.update_recipe(request.form)
    return redirect('/recipes')



@app.route('/recipes/<int:id>')
def view_recipe(id):
    if 'uuid' not in session:
        return redirect('/')
    data = {
        "id":id
    }
    return render_template("view_recipe.html", recipe=Recipe.get_recipe_with_user(data))

@app.route('/recipes/destroy/<int:id>')
def destroy(id):
    if 'uuid' not in session:
        return redirect('/')
    data ={
        'id': id
    }
    Recipe.destroy(data)
    return redirect('/recipes')