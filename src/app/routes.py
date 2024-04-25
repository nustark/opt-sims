
from flask import Blueprint, render_template, session, abort, jsonify, request
from app.database import option_collection

app_routes = Blueprint('app_routes', __name__)


@app_routes.route("/")
def hello():
    return "Hello World!"


@app_routes.route('/api/options', methods=['GET'])
def get_options():
    # Fetch options data from MongoDB
    options_data = list(option_collection.find())
    return jsonify(options_data)


@app_routes.route('/api/trade', methods=['POST'])
def execute_trade():
    trade_data = request.json
    # implement logic to execute trades based on trade_data
    # example: mongo.db.transactions.insert_one(trade_data)
    return jsonify({"message": "Trade executed successfully"})