

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.pw = data['pw']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

@classmethod
def create(cls, data):
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
    user_id = connectToMySQL('users_schema').query_db(query, data)
    return user_id

@classmethod
def get_all(cls):
    query = "SELECT * FROM users;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
    results = connectToMySQL('users_schema').query_db(query)
    # Create an empty list to append our instances of friends
    all_users = []
    # Iterate over the db results and create instances of friends with cls.
    for user in results:
        all_users.append( cls(user) )
    return all_users

@staticmethod
# data is the request.form ...
def validate(data):
    is_valid = True

    if len(data['first_name']) <1:
        flash('first name is required', 'err_user_first_name')
        is_valid = False

    if len(data['last_name']) <1:
        flash('last name is required', 'err_user_last_name')
        is_valid = False
        
    if len(data['email']) <1:
        flash('email is required', 'err_user_email')
        is_valid = False
                
    return is_valid