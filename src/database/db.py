import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

env_file = find_dotenv('.env')
load_dotenv(env_file)

cluster = MongoClient(os.environ.get('MONGODB_ATLAS_URI'))
db = cluster[os.environ.get('MONGO_ATLAS_CLUSTER_NAME')]
option_collection = db[os.environ.get('MONGO_ATLAS_COLLECTION_OPTION')]
user_collection = db[os.environ.get('MONGO_ATLAS_COLLECTION_USER')]
transaction_collection = db[os.environ.get(
    'MONGO_ATLAS_COLLECTION_TRANSACTION')]
