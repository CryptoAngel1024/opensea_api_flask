from distutils.log import debug
from pickle import TRUE
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_pymongo import pymongo
from flask_cors import CORS, cross_origin
import requests

parser = reqparse.RequestParser()
parser.add_argument("type", type = str, help = "Type of the product", location='args')

CONNECTION_STRING="mongodb+srv://simon:tiger%401024@cluster0.io9kc.mongodb.net/test"

client = pymongo.MongoClient(CONNECTION_STRING)
app = Flask(__name__)

CORS(app)
api = Api(app)

app.url_map.strict_slashes = False # Disable redirecting on POST method from /star to /star/
class CollectionBySlug(Resource):
  def get(self, collection_slug):
    response = requests.get(url="https://api.opensea.io/api/v1/collection/" + collection_slug)
    return jsonify({'data' : response.json()})

class Collection(Resource):
  def get(self):
    args = parser.parse_args()
    output = []
    listed_collection = []
    for data in client.test.list.find({ "collection_slug": args['type'] }):
      listed_collection.append({
        '_id': str(data['_id']),
      })

    for data in client.test.sold.find({ "collection_slug": args['type'] }).sort("timestamp", -1):
      output.append({
        '_id': str(data['_id']),
        'timestamp': data['timestamp'], 
        'collection_slug': data['collection_slug'], 
        'quantity': data['quantity'], 
        'price': data['price'], 
        'listed_assets': len(listed_collection),
      })
    return jsonify({'result' : output})

api.add_resource(CollectionBySlug, '/collections/<string:collection_slug>')  
api.add_resource(Collection, '/collection')  

if __name__ == '__main__':
  app.run(debug=TRUE)