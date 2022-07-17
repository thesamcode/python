

# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
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


    # C
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

    # U
    # D

    # create
    # get_all
    # get_many
    # get_one
    # update_one
    # update_many
    # delete_one
    # delete_many