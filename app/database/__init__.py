from mongoengine import connect
from core import settings
from enum import Enum
import asyncio

class Collections(Enum):
    users = 'users'
    cars = 'cars'


# Creating connection and database
localSettings = settings.Settings()
connect(localSettings.mongoDBName,
        username=localSettings.MongoUser,
        password=localSettings.MongoSecret,
        host=localSettings.mongouri)



