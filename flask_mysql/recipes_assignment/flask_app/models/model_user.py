
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import model_user
from flask import flash, session
import re
from flask_app import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('recipes_schema').query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False

    @classmethod
    def get_one_by_email(cls, data:dict) -> list:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        if results:
            return cls(results[0])
        return False

    # @classmethod
    # def get_recipe_with_users (cls):
    #     query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
    #     results = connectToMySQL('recipes_schema').query_db(query)
    #     all_recipes = []
    #     # results will be a list of topping objects with the burger attached to each row. 
    #     for row_from_db in results:
    #         recipe = cls(row_from_db)
    #         # Now we parse the burger data to make instances of burgers and add them into our list.
    #         user_data = {
    #             "id": row_from_db["users.id"],
    #             "first_name": row_from_db["first_name"],
    #             "last_name": row_from_db["last_name"],
    #             "email": row_from_db["email"],
    #             "created_at": row_from_db["users.created_at"],
    #             "updated_at": row_from_db["users.updated_at"]
    #         }
    #         # recipe.users.append(model_user.User(user_data))
    #         recipe.user=User(user_data)
    #         all_recipes.append(recipe)
    #     return all_recipes

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        # comes back as the new row id
        result = connectToMySQL('recipes_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.", 'err_users_first_name')
            is_valid = False

        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.", 'err_users_last_name')
            is_valid = False

        if len(data['email']) < 2:
            flash("Email must be correct format.", 'err_users_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address.", 'err_users_email')
            is_valid = False
        else:
            potential_user = User.get_one_by_email({'email': data['email']})
            if potential_user:
                flash("Email already in use.", 'err_users_email')
                is_valid = False

        if len(data['password']) < 2:
            flash("Must create password.", 'err_users_password')
            is_valid = False

        if len(data['password_confirm']) < 2:
            flash("Passwords must match.", 'err_users_password_confirm')
            is_valid = False
        elif data['password'] != data['password_confirm']:
            flash('Passwords do not match.', 'err_users_password_confirm')

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True

        if len(data['email']) < 2:
            flash("Field is required.", 'err_users_login')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email", 'err_users_login')
            is_valid = False
        else:
            potential_user = User.get_one_by_email({'email': data['email']})
            if not potential_user:
                flash("Invalid credentials!", 'err_users_login')
                is_valid = False
            # check hash
            elif not bcrypt.check_password_hash(potential_user.password, data['password']):
                flash("Invalid credentials!!", 'err_users_login')
                is_valid = False
                # store the id for the session
            else:
                # can't store the whole user session into the instance. Can just odo the id...
                session['uuid'] = potential_user.id

        if len(data['password']) < 2:
            flash("Field is required.", 'err_users_login_password')
            is_valid = False
        print(is_valid)
        return is_valid