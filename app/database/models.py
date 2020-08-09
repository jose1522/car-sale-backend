from mongoengine import *
from .validation import  *
from core.util.message import *
from core.util.authentication import *
import json


class User(Document):
    email = StringField(max_length=120, required=True, unique=True)
    name = StringField(max_length=120, required=True)
    firstLastName = StringField(max_length=120, required=True)
    secondLastName = StringField(max_length=120, required=False)
    state = StringField(max_length=120, required=True)
    city = StringField(max_length=120, required=True)
    neighborhood = StringField(max_length=120, required=True)
    address = StringField(max_length=120, required=True)
    password = StringField(max_length=120, required=True)
    phone = IntField(required=True)
    identification = IntField(required=True, unique=True)

    @classmethod
    async def createUser(cls, newUser: NewUserParams):
        msg = Message()
        try:
            doc = cls()
            newUser = dict(newUser)
            for key, value in newUser.items():
                if value is not None:
                    if key == 'password':
                        value = get_hashed_password(value)
                    doc.__setattr__(key, value)
            doc.save()
            msg.addMessage('Data', json.loads(doc.to_json()))
            return msg.data
        except Exception as e:
            msg.addMessage('Error', str(e))
            return msg.data

    @classmethod
    async def updateUser(cls, currentUser, newData: UserParams):
        msg = Message()
        try:
            newData = dict(newData)
            doc = cls.objects.get(email=currentUser.get('email'))
            for key, value in newData.items():
                if value is not None and key != 'email':
                    if key == 'password':
                        value = get_hashed_password(value)
                    doc.__setattr__(key, value)
            doc.save()
            msg.addMessage('Data', json.loads(doc.to_json()))
            return msg.data
        except Exception as e:
            msg.addMessage('Error', str(e))
            return msg.data

    @classmethod
    async def deleteUser(cls, currentUser):
        msg = Message()
        try:
            doc = cls.objects.get(email=currentUser.get('email'))
            doc.delete()
            msg.addMessage('Success', True)
            return msg.data
        except Exception as e:
            msg.addMessage('Success', False)
            msg.addMessage('Error', str(e))
            return msg.data

    @classmethod
    async def authenticate(cls, inputCredentials: AuthParams):
        try:
            msg = await check_password(inputCredentials)
            return msg.data
        except Exception as e:
            msg = AuthMessage()
            msg.authResult(False)
            msg.addMessage('Error', str(e))
            return msg.data

    @classmethod
    async def getByEmail(cls, email: str):
        try:
            result = cls.objects.get(email=email).to_json()
            result = json.loads(result)
            return result
        except Exception as e:
            print(str(e))
            return []


class Car(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    brand = StringField(max_length=120, required=True)
    color = StringField(max_length=120, required=True)
    model = StringField(max_length=120, required=True)
    km = StringField(max_length=120, required=True)
    plate = StringField(max_length=120, required=True)
    year = StringField(max_length=120, required=True)
    transmission = StringField(max_length=120, required=True)
    extras = StringField(max_length=120, required=False)
    photos = ListField(StringField(max_length=250, required=False))