

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello')
def hello_jim():
    return 'Hello Jim!'

@app.route('/name/<name>')
def name(name):
    print(name)
    return f"Hello {name}!"

@app.route('/name/<name>/<int:age>')
def name_age(name, age):

    #render template page and pass in variables as keyword arguments (kwargs)
    return render_template('people.html', name1 = name, age1 = age)
    # return f"Hello! I'm {name} and I'm {age} years old!"

# @app.route('/name/<name>/<age>')
# def name_age2(name, age):
#     age = age + " johnny"
#     return f"Hello! I'm {name} and I'm {age} years old!"


# THIS NEEDS TO BE ON THE BOTTOM FO THE FILE
if __name__=="__main__":
    app.run(debug=True)