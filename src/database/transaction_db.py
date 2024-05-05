from database.db import transaction_collection


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
