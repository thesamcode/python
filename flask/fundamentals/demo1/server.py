

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "aaabbbcccddeeffggghhh"


@app.route('/')
# this is a dispaly route
def hello_world():
    name = "tyler"
    return render_template('index.html', name=name)

# if there are multiple, then methods, if single, then method
@app.route('/process_info', methods=['POST'])
def process_info():
    print(f"You have now purchased a new {request.form['item']}")
    # credit_card_number = request.form['credit_card_number']

    session['ccn'] = str(request.form['credit_card_number'])[-4:]
    # session works similar to the bottom for setting things into session or pulling them up
    # data = {}
    # data['name'] = 'tyler'
    # data['name']

    # print("This Worked")
    # not what we want to do. this is an action route
    # NEVER RENDER ON ACTION FORM. JUST REDIRECT
    # return render_template('index.html')
    return redirect('/tracking_info')

# @app.route('/<int:row>/<int:col>')
# def row(row, col):

# you cannot pass paramteres through a redirect
@app.route('/tracking_info')
def tracking_info():
    print("Your card number is:")
    # will ask if the key is in our session
    if 'ccn' not in session:
        return redirect('/')
    # print(session['ccn'])
    return render_template('tracking.html')



#     #render template page and pass in variables as keyword arguments (kwargs)
#     return render_template('checker.html', rows = row, cols = col)

# THIS NEEDS TO BE ON THE BOTTOM FO THE FILE
if __name__=="__main__":
    app.run(debug=True)