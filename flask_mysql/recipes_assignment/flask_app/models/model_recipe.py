
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_user
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.user = {}
        self.users = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        all_recipes = []
        for recipe in results:
            all_recipes.append( cls(recipe) )
        return all_recipes

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_cooked, under_30, user_id) VALUES (%(name)s,%(description)s,%(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s);"

        # comes back as the new row id
        result = connectToMySQL('recipes_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_recipe_with_users (cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL('recipes_schema').query_db(query)
        all_recipes = []
        # results will be a list of topping objects with the burger attached to each row.
        if results:
            for row_from_db in results:
                recipe = cls(row_from_db)
                # Now we parse the burger data to make instances of burgers and add them into our list.
                user_data = {
                    "id": row_from_db["users.id"],
                    "first_name": row_from_db["first_name"],
                    "last_name": row_from_db["last_name"],
                    "email": row_from_db["email"],
                    "password": row_from_db["password"],
                    "created_at": row_from_db["users.created_at"],
                    "updated_at": row_from_db["users.updated_at"]
                }
                # recipe.users.append(model_user.User(user_data))
                recipe.user=model_user.User(user_data)
                all_recipes.append(recipe)
            return all_recipes
        return []

    @classmethod
    def get_recipe_with_user (cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        # results will be a list of topping objects with the burger attached to each row. 
        recipe = cls(results[0])
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            user_data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            recipe.users.append(model_user.User(user_data))
        return recipe

    @classmethod
    def update_recipe(cls, data:dict) -> None:
        # in the below line, we needed to match the "recipe_id" to the variable in the controller. but it is a number and it matches the database id number so they are used for referencing.
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, under_30=%(under_30)s WHERE id = %(recipe_id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 3:
            flash("Recipe name must be at least 3 characters.", 'err_recipes_name')
            is_valid = False

        if len(data['description']) < 3:
            flash("Description must be at least 3 characters.", 'err_recipes_description')
            is_valid = False

        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.", 'err_recipes_instructions')
            is_valid = False

        if len(data['date_cooked']) < 1:
            flash("Cooked/made date required.", 'err_recipes_date_cooked')
            is_valid = False
        
        ## DATE FIELD FIGURE IT OUT

        return is_valid