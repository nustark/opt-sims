
import json
from flask import Blueprint, render_template, session, abort, jsonify, request, redirect, url_for
from flask_dance.contrib.google import google
from pydantic import ValidationError
from app.database import option_collection, OptionDatabase, UserDatabase, TransactionDatabase
from charts.module1 import query_ticker
from trade_engine.module2 import OptionData


app_routes = Blueprint('app_routes', __name__)
option_db = OptionDatabase()
user_db = UserDatabase()
transact_db = TransactionDatabase


@app_routes.route("/")
def login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    return "Hi {email}, welcome to Optionz, your favorite paper trading tool".format(email=resp.json()["email"])


@app_routes.route('/api/options', methods=['GET'])
def get_options():
    try:
        options = option_db.get_all_options()
        return jsonify(json.loads(json.dumps(options, default=str))), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app_routes.route('/api/trade', methods=['POST'])
def execute_trade():
    try:
        trade_data = OptionData(**request.json)
        option_db.insert_option(trade_data.dict())
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    print(trade_data.dict())
    return jsonify({"message": "Trade executed successfully"})


@app_routes.route('/api/chart/getInfo', methods=['GET'])
def get_chart():
    try:
        ticker_symbol = request.args.get('ticker')
        return query_ticker(ticker_symbol).json(), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
