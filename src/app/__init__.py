import os
# from flask_pymongo import PyMongo
# from dotenv import load_dotenv, find_dotenv
# from pymongo import MongoClient
# from flask import Flask, jsonify, request

from flask import Flask
from app.routes import app_routes

# env_file = find_dotenv(".env")
# load_dotenv(env_file)

app = Flask(__name__)

app.register_blueprint(app_routes)

# cluster = MongoClient(os.environ.get("MONGODB_ATLAS_URI"))

# db = cluster["optionz-db-dev"]

# option_collection = db['option']

# for document in option_collection.find():
#     print(document)


# @app.route("/")
# def hello():
#     return "Hello World!"


# @app.route('/api/options', methods=['GET'])
# def get_options():
#     # Fetch options data from MongoDB
#     options_data = list(option_collection.find())
#     return jsonify(options_data)


# @app.route('/api/trade', methods=['POST'])
# def execute_trade():
#     trade_data = request.json
#     # implement logic to execute trades based on trade_data
#     # example: mongo.db.transactions.insert_one(trade_data)
#     return jsonify({"message": "Trade executed successfully"})
