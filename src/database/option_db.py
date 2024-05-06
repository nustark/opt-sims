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

    def get_options_by_user_id(self, user_id) -> list:
        try:
            if user_id:
                return list(self.collection.find({'user_id': user_id}))
            else:
                print('User ID not found in session')
                return []
        except Exception as e:
            print(f'Error retrieving options by user ID: {e}')
            return []
