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


class OptionDatabase:
    def __init__(self):
        self.collection = option_collection

    def insert_option(self, trade_data) -> None:
        try:
            self.collection.insert_one(trade_data)
        except Exception as e:
            print(f'Error inserting option data: {e}')

    def get_all_options(self) -> list:
        try:
            return list(self.collection.find())
        except Exception as e:
            print(f'Error retrieving options: {e}')
            return []


class UserDatabase:
    def __init__(self):
        self.user_collection = user_collection

    def insert_user(self, user_data) -> None:
        try:
            self.user_collection.insert_one(user_data)
        except Exception as e:
            print(f"Error inserting user data: {e}")

    def get_all_users(self) -> list:
        try:
            return list(self.user_collection.find())
        except Exception as e:
            print(f"Error retrieving users: {e}")
            return []


class TransactionDatabase:
    def __init__(self):
        self.transaction_collection = transaction_collection

    def insert_transaction(self, transaction_data) -> None:
        try:
            self.transaction_collection.insert_one(transaction_data)
        except Exception as e:
            print(f"Error inserting transaction data: {e}")

    def get_all_transactions(self) -> list:
        try:
            return list(self.transaction_collection.find())
        except Exception as e:
            print(f"Error retrieving transactions: {e}")
            return []
