
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append( cls(dojo) )
        return all_dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        # comes back as the new row id
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_dojo_with_ninjas (cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls(results[0])
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "dojo_id": row_from_db["dojo_id"],
                "dojo_name": row_from_db["dojo_name"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(model_ninja.Ninja(ninja_data))
        return dojo

        # 