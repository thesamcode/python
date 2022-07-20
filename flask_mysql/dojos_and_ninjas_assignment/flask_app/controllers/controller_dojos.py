
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    return render_template("dojos.html", all_dojos=Dojo.get_all())

@app.route('/dojos/create_dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id":id
    }
    return render_template("dojo_show.html", dojo=Dojo.get_dojo_with_ninjas(data))