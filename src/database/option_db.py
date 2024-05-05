from database.db import option_collection


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
