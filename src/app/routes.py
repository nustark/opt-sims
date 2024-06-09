
import json
from flask import Blueprint, render_template, session, abort, jsonify, request, redirect, url_for
from flask_dance.contrib.google import google
from pydantic import ValidationError
from database.option_db import OptionDatabase
from database.transaction_db import TransactionDatabase
from database.user_db import UserDatabase
from charts.alpha_vantage import query_ticker, query_ticker_by_date
from trade_engine.models import OptionData
from trade_engine.util_functions import *


app_routes = Blueprint('app_routes', __name__)
option_db = OptionDatabase()
user_db = UserDatabase()
transact_db = TransactionDatabase

'''
server routes
'''


@app_routes.route("/")
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    # return "Hi {email}, welcome to Optionz, your favorite paper trading tool".format(email=resp.json()["email"])
    email = resp.json()["email"]
    user_doc = user_db.get_user_by_email(email)

    if user_doc:
        session['user_id'] = int(user_doc['_id'])
        return f"Hi {user_doc['display_name']} (id: {user_doc['_id']}), welcome to Optionz, your favorite paper trading tool"
    else:
        # Handle the case where the user is not found in the database
        return "User not found in the database"


'''
db crud routes
'''


@ app_routes.route('/api/options', methods=['GET'])
def get_options():
    try:
        user_id = session.get('user_id')
        options = option_db.get_valid_options_by_user_id(user_id)
        return jsonify(json.loads(json.dumps(options, default=str))), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@ app_routes.route('/api/trade', methods=['POST'])
def insert_trade():
    try:
        trade_data = OptionData(**request.json)
        option_db.insert_option(trade_data.dict())
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    print(trade_data.dict())
    return jsonify({"message": "Trade inserted successfully in database"})


'''
trade engine routes
'''


@ app_routes.route('/api/trade/execute', methods=['POST'])
def execute_trade():
    try:
        trade_data = OptionData(**request.json)
        # fetch ticker data from alphavantage, pass into util function
        # hard-coded execution price/date
        calculate_option_profit(trade_data, 125.00, datetime(2023, 6, 15))
        option_db.insert_option(trade_data.dict())
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    print(trade_data.dict())
    return jsonify({"message": "Trade executed successfully"})


'''
data/chart ticker routes
'''


@ app_routes.route('/api/chart/getInfo', methods=['GET'])
def get_chart():
    try:
        ticker_symbol = request.args.get('ticker')
        return query_ticker(ticker_symbol).json(), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@ app_routes.route('/api/chart/getInfoByDate', methods=['GET'])
def get_chart_by_date():
    try:
        ticker_symbol = request.args.get('ticker')
        return query_ticker_by_date(ticker_symbol, '1'), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
