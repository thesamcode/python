

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.numandstreet = data['numandstreet']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        self.pw = data['pw']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"


    # C
    #  This creates the user
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, numandstreet, city, state, zip, pw) VALUES (%(first_name)s, %(last_name)s, %(numandstreet)s, %(city)s, %(state)s, %(zip)s, %(pw)s);"
        user_id = connectToMySQL('event_planner').query_db(query, data)
        return user_id
    # R
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('event_planner').query_db(query)
        # Create an empty list to append our instances of friends
        all_users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            all_users.append( cls(user) )
        return all_users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # still a list first with dictionary inside
        result = connectToMySQL('event_planner').query_db(query, data)

        if result:
            user = cls(result[0])
            return user
        return False

    # U
    # D

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
        
        if len(data['numandstreet']) <1:
            flash('street number and street name required', 'err_user_num_and_street')
            is_valid = False
        
        if len(data['city']) <1:
            flash('city required', 'err_user_city')
            is_valid = False

        if len(data['state']) <1:
            flash('state required', 'err_user_state')
            is_valid = False    
        
        if len(data['zip']) <1:
            flash('zip code required', 'err_user_zip')
            is_valid = False

        if len(data['pw']) <1:
            flash('password is required', 'err_user_pw')
            is_valid = False            

        
        return is_valid

    @staticmethod
    # data is the request.form ...
    def validate_login(data):
        is_valid = True
        
        if len(data['pw']) < 1:
            flash('password is required', 'err_user_pw')
            is_valid = False
        else:
            potential_user = User.get_one({'id': data['id']})
            if not bcrypt.check_password_hash(potential_user.pw, data['pw']):
                flash("Incorrect Password", 'err_user_pw_login')
                is_valid = False

        
        return is_valid

    # if len(data['email']) < 1:
    #     flash("email is required", 'err_user_email')
    #     is_valid = False

    # elif not EMAIL_REGEX.match(data['email']):
        # flash('invalid email address', 'err_user_email')
        # is_valid = False


    # if len(data['phone_num']) < 10:
    #     flash("phone number is required", 'err_user_phone_num')
    #     is_valid = False

    # elif int(data['phone_num']) > 4294967295:
    #     flash("phone number is too long", 'err_user_phone_num')
    #     is_valid = False

    # create
    # get_all
    # get_many
    # get_one
    # update_one
    # update_many
    # delete_one
    # delete_many