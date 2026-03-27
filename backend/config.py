from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) #initialising the app
CORS(app) #now our backend is accesible to anyone

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # give us a db instance to use it