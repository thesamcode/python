

# Setting up Flask App

-Create project/assignment folder

-Navigate into folder
```
cd project_name
```
-install virtual environment with flask, mysql, and bcrypt
```
pipenv install flask pyMySQL flask-bcrypt
```
(look for the pipfile and pipfile.lock)

-launch shell
```
pipenv shell
python server.py
```
- Build files and folders
    - project (folder)
        - flask_app (folder)
            - config (folder)
                - mysqlconnection.py (file)
            - controllers (folder)
                - controller_user.py (file)
            - models (folder)
                - model_user.py (file)
            - static (folder)
                - css (folder)
                    -style.css (file)
                - js (folder)
                    - script.js (file)
            - templates (folder)
                - index.html (file)
                - table_name_action.html (file)
                - user_new.html (file)
                - user_edit.html (file)
            - \_\_init__.py (file)
        - pipfile (file)(auto)
        - pipfile.lock (file)(auto)
        - server.py (file)

## mysqlconnection.py
```py
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            # try will try everything inside the try
            try:
                # passing in data and query to combine them into the query variable
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query)
                # that insert word and the select word are the same ones used in mysql
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            # if there is an error then it runs this
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```
## controller_user.py
```py
from flask_app import app
from flask import render_template, redirect, session, request

#This imports the model file
#from flask_app.models import_model_table_name

# Display route
@app.route('/table_name/new)
def table_name_new():
    return render_template('table_name_new.html')

@app.route('/table_name/create', methods=['POST'])
def

```
## model_user.py

```py
#import the function 


MORE STUFF HERE... ... ... .. .. ... ... ... .. ... ... .. ... .
```
## index.html file

```
template stuff
```
## \_\_init.__.py file
```py
from flask import Flask
app = Flask(__name)
app.secret_key = "123456"
# DATABASE = "schema_name"

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
```

## server.py file material

```py
from flask_app import app
# Remember to continually add controller files as you create them
```
