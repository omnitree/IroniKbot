import mongoengine
import os
from Bot_DB.Mango.database_models import User, Users

class database_connection:
    def __init__(self):
        self.db_username = os.environ.get('DB_USERNAME')
        self.db_password = os.environ.get('DB_PASSWORD')
        self.db_host = os.environ.get('DB_HOST')
        self.db_name = os.environ.get('DB_NAME')

    def get_connection(self):
        return mongoengine.connection

    def connect(self, client):
        mongoengine.connect(self.db_name,
                            username=self.db_username,
                            password=self.db_password,
                            host=self.db_host)
        self.client = client


    def load_users(self):
        count = 0
        print("Loading all the users...")
        for user in self.client.get_all_members():
            try:
                User_tmp = User(user_id=int(user.id), exp=0).save()
            except mongoengine.NotUniqueError:
                pass
