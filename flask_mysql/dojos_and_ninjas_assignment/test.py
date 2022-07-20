

@app.route('/dojos/<int:id>')
def view(id):
    data = {
        "id":id
    }
    return render_template("dojo_show.html", ninja=Ninja.get_one(data))