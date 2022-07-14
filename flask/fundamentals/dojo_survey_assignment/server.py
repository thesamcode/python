
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "aaabbbcccddeeffggghhh"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def process_info():
    session['name'] = str(request.form['your_name'])
    session['dojoloc'] = str(request.form['dojo_location'])
    session['favlang'] = str(request.form['language'])
    session['com'] = str(request.form['comment'])
    return render_template('results.html')


if __name__=="__main__":
    app.run(debug=True)