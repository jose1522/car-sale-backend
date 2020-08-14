from mongoengine import connect
from core import settings
from enum import Enum
import asyncio

class Collections(Enum):
    users = 'users'
    cars = 'cars'


# Creating connection and database
localSettings = settings.Settings()
connect(db=localSettings.mongoDBName,
        authentication_source='admin',
        username=localSettings.MongoUser,
        password=localSettings.MongoSecret,
        host=localSettings.mongouri)



