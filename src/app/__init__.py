import os
from flask import Flask
from flask_dance.contrib.google import make_google_blueprint
from dotenv import load_dotenv, find_dotenv
from app.routes import app_routes


env_file = find_dotenv('.env')
load_dotenv(env_file)

app = Flask(__name__)

app.secret_key = os.environ.get('NOT_FLASK_SECRET_KEY')
# print(os.environ.get('MONGODB_ATLAS_USER'))
# print(os.environ.get('NOT_FLASK_SECRET_KEY'))
# print(os.environ.get('FLASK_SECRET_KEY'))
# app.secret_key = '23'

google_bp = make_google_blueprint(
    client_id=os.environ.get('GOOGLE_API_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_API_CLIENT_SECRET'),
    scope=["profile", "email"],
    offline=True
)

app.register_blueprint(google_bp, url_prefix="/login")

app.register_blueprint(app_routes)
