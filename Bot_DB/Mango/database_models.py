import datetime

import mongoengine


class User(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True)
    exp = mongoengine.IntField()


class Users(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True)
    exp = mongoengine.LongField()
    multiplier = mongoengine.IntField(min_value=1, max_value=3, default=1)
    time_stamp = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    level = mongoengine.IntField(default=1,min_value=1)
