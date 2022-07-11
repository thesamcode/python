

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello_jim():
    return 'Hello Jim!'

@app.route('/name/<name>')
def name(name):
    print(name)
    return f"Hello {name}!"

@app.route('/name/<name>/<int:age>')
def name_age(name, age):
    age = age + 10
    return f"Hello! I'm {name} and I'm {age} years old!"

@app.route('/name/<name>/<age>')
def name_age2(name, age):
    age = age + " johnny"
    return f"Hello! I'm {name} and I'm {age} years old!"


# THIS NEEDS TO BE ON HE BOTTOM FO THE FILE
if __name__=="__main__":
    app.run(debug=True)