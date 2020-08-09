import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        load_dotenv()
        self.apiToken = os.environ.get('Token-Secret')
        self.mongouri = os.environ.get('MongoURI')
        self.mongoDBName = os.environ.get('MongoDBName')
        self.MongoUser = os.environ.get('MongoUser')
        self.MongoSecret = os.environ.get('MongoSecret')
        self.MongoSecret = os.environ.get('MongoSecret')
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.ALGORITHM = os.environ.get('ALGORITHM')