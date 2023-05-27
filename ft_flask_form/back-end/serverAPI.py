""" Login/Reg form in full-stack python
    1. Front-end => Flet (Python)
    2. Back-end => Flask (Python)
    3. Database => sql alchemy (python)

"""

""" 
Make a folder called "root"
two sub folder= back-end + front-end 
two files wihtin each, serverAPI.py and client.py

"""

""" Starting with the server file"""

""" The modules we need 
    This is also a basic flask app set up 
"""
from enum import unique
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

""" set the db object as sqlalchemy"""
db = SQLAlchemy()


def CreateUUID():
    return uuid4().hex


""" First we create a model which will represent the database"""
""" name the class and pass the db.MOdel module"""


class User(db.Model):
    """the table name"""

    __tablename__ = "users"
    """ automatic ID generator
        CreateUUID is a function above which generates a hex UUID
    """
    id = db.Column(db.String(32), unique=True, primary_key=True, default=CreateUUID)

    """ email column, make sure it's set to unique"""
    email = db.Column(db.String(355), unique=True)

    """ passowrd column, make sure nullable is false"""
    password = db.Column(db.String(), nullable=False)


""" Second, we want to configure the back-end with some sql alchemy attributes, such as ECHO which shows what's happening in the database as well as generating a db file and storing it in this current directoy"""


class AppConfiguration:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLACLCHEMY_ECHO = True
    """ Most important: this generates a sqlite db file in the current directory"""
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"


""" start the app/server """
app = Flask(__name__)
app.config.from_object(AppConfiguration)
db.init_app(app)

""" How to set up the registration route"""
# set the url to /registration with the POST method
@app.route("/register", methods=["POST"])
def RegisterUser():
    # we store the incoming data in a variable as json data
    user_data = request.get_json()
    # we then create another variable and call the User => db model and pass the json data into it.
    # recall that the USER model has two columns, emai land password, and we can easily set each by parsing the JSON object
    user = User(email=user_data["email"], password=user_data["password"])
    # add the user to the db and commit
    db.session.add(user)
    db.session.commit()

    # we can return a 201 which is a status ok.
    return "done", 201


# Login route for the Python API
# Set the correct route and method
@app.route("/login", methods=["POST"])
def LogIn():
    # we get two arguments, email and passowrd as json type
    email = request.json["email"]
    password = request.json["password"]

    # first step => filter the User datbase by email
    user = User.query.filter_by(email=email).first()

    # if the email is not in the database, we return an error
    if user is None:
        return jsonify({"error": "Invalid email"}), 401
    # when we enter an invalid email, we get a 401 response

    # second, we check if the passowrds match/or don't match in this case
    if user.password != password:
        return jsonify({"error": "Invalid password"}), 401
    # again, even if the email is right, if the passowrd isn't it thorws a 401

    # if all is true, the server returns a 201
    return jsonify({"OK": "Login successful"}), 201


""" this alows us to use  the server wihtot having it online"""
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

""" notice the db being created in the directory"""
