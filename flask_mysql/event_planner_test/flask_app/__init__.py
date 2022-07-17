
from flask import Flask
from flask_bcrypt import Bcrypt    
# from friend import Friend

app = Flask(__name__)
app.secret_key = "aaabbbccc"

bcrypt = Bcrypt(app)