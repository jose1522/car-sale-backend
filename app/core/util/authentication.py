from datetime import datetime, timedelta
from typing import Optional
from database.validation import *
from database import models
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.settings import *
from core.util.message import AuthMessage
import bcrypt
import base64
import hashlib

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_hashed_password(password: str):
    password = password.encode('utf8')
    password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf8')
    return password


async def check_password(inputCredentials: AuthParams):
    msg = AuthMessage()

    # transform input
    inputCredentials = dict(inputCredentials)

    # get user by email
    inputPassword = inputCredentials.get('password').encode('utf8')
    user = await models.User.getByEmail(inputCredentials.get('email'))
    userPassword = user.get('password').encode('utf8')

    # check passwords
    result = bcrypt.checkpw(inputPassword, userPassword)
    msg.authResult(result)

    # add token if the passwords match
    if result:
        token = create_access_token(user)
        msg.addMessage('Token', token)
    return msg


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    localSettings = Settings()
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(weeks=2)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, localSettings.SECRET_KEY, algorithm=localSettings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str):
    localSettings = Settings()
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, localSettings.SECRET_KEY, algorithms=[localSettings.ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await models.User.getByEmail(email)
    if len(user) == 0:
        raise credentials_exception
    else:
        del user['password']
        return user
