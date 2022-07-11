
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "aaabbbcccddeeffggghhh"

# counter = 0

@app.route('/')
# this is a dispaly route
def main():
    # global counter
    # session['count'] = 0
    session['count'] += 1
    # counter += 1
    # session['count'] = str(counter)
    # return render_template(str(counter))
    return render_template('index.html')

# @app.route('/')
# # this is a dispaly route
# def hello_world():
#     return render_template('index.html')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    # session['clear'] = str(session.clear())
    session.clear()
    session['count'] = 0
    # counter = 0
    print(session['count'])
    return redirect('/')













if __name__=="__main__":
    app.run(debug=True)