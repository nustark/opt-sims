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


# def insert_option(trade_data):
#     option_collection.insert_one(trade_data)

class OptionDatabase:
    def __init__(self):
        self.collection = option_collection

    def insert_option(self, trade_data) -> None:
        try:
            self.collection.insert_one(trade_data)
        except Exception as e:
            print(f"Error inserting option data: {e}")

    def get_all_options(self) -> list:
        try:
            return list(self.collection.find())
        except Exception as e:
            # Handle the exception and log the error
            print(f"Error retrieving options: {e}")
            return []
