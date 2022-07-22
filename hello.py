from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://dev:opensea2022.@orca.8feyo.mongodb.net/test"
mongo = PyMongo(app)