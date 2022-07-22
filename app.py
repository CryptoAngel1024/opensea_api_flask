from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route('/', methods=['GET'])
def opensea_api():
  data = db.trades.find()
  return jsonify({'result': data})

if __name__ == '__main__':
  app.run(debug=True)
