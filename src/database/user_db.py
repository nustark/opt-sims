from database.db import user_collection


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
