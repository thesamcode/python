

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<int:row>/<int:col>')
def row(row, col):

    #render template page and pass in variables as keyword arguments (kwargs)
    return render_template('checker.html', rows = row, cols = col)

# THIS NEEDS TO BE ON THE BOTTOM FO THE FILE
if __name__=="__main__":
    app.run(debug=True)