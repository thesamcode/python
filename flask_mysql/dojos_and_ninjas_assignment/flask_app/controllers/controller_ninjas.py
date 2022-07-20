
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo


@app.route('/ninja/new')
def new():
    return render_template("new_ninja.html", all_dojos=Dojo.get_all())

@app.route('/ninja/create_ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/dojos')