import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

env_file = find_dotenv(".env")
load_dotenv(env_file)

cluster = MongoClient(os.environ.get("MONGODB_ATLAS_URI"))

db = cluster["optionz-db-dev"]

option_collection = db['option']

for document in option_collection.find():
    print(document)
