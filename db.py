from http import client
from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING="mongodb+srv://dev:opensea2022.@orca.8feyo.mongodb.net/test"
client = pymongo.MongoClient(CONNECTION_STRING)
print(client.list_database_names())
db = client.get_database('opensea')
trades = pymongo.collection.Collection(db, 'trades')