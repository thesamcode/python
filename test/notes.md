Python vs Javascript

-Data Types
    -Integers, Floats
    -String
    -Boolean
    -Arrays
    -Objects
    -Tuples
-Loops
-Conditionals
-Functions

## Numbers

- 35 -> 35.0
integer vs float


| js | py |
| --- | --- |

first_name = "tyler"
y = "2"

arrays -> list

``` py
brothers = ['tyler', 'curtis', 'joe']
```
objects are called dictionary in python

in js - used as key - value pairs. Key is anchor point value is return of info.

```js
function add)num1,num2){return num1 + num2}

add(2,3)
```
```py
def add(num1, num2):
    return num1 + num2

add(2,3)
```
-----2022 July 6 

# Object Oriented programming

- classes
    - constructor
    - attributes
    - methods
    -self

self is targeting an instance of a class
## Class
What is a class?
- blueprint

## constructor
- magic method
def \_\_init__()
this returns an instance of th emethod

## Attributes
`distinguishing characteristics of the object`
`the things that make up and object`
- make
- model
- color
- price
- number of seats
- number of doors

# Methods
`performs some action on the object`
is functions inside of classes
- drive 
- turn on
- turn off
- lock
- increase odometer -> distance

## self
`refers to instance of the object`


FLASK basic code

# Pre-rec
```
pip install pipenv
pipenv install flask (IN DESIRED LOCATION FOLDER)

launch virtual env
pipenvshell
```
mkdir makes a folder and touch makes a file
need assignment folders for assignments
rm -r -f assignmnet.txt and MAKE SURE YOU ARE IN THE RIGHT FOLDER

1. create folder/directory for assignment
2. navigate into the folder
3. create virtual environment
    install pipemv
LOOK FOR pipfile and pipfile.lock

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


// THIS NEEDS TO BE ON HE BOTTOM FO THE FILE
if __name__=="__main__":
    app.run(debug=True)


localhost:5000
127.0.0.1:5000

view it locally

ctrc c in the command prompt will stop the server
press up arrow to restart with server.py

pip freeze

shows dependencies

pipenvshell
launches the environment


