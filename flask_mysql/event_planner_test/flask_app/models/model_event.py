



# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Event:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.location = data['location']
        self.description = data['description']
        self.start_time = data['start_time']
        self.end_time = data['end_time']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"


    # C
    #  This creates the user
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (title, location, description, start_time, end_time) VALUES (%(title)s, %(location)s, %(description)s, %(start_time)s, %(end_time)s);"
        event_id = connectToMySQL('event_planner').query_db(query, data)
        return event_id
    # R
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM events;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('event_planner').query_db(query)
        # Create an empty list to append our instances of friends
        all_events = []
        # Iterate over the db results and create instances of friends with cls.
        for event in results:
            all_events.append( cls(event) )
        return all_events

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