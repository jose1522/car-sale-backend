from pydantic import BaseModel
from typing import Optional


class NewUserParams(BaseModel):
    email: str
    name: str
    firstLastName: str
    secondLastName: Optional[str] = None
    state: str
    city: str
    neighborhood: str
    address: str
    password: str
    phone: int
    identification: int
    id: Optional[str]


class UserParams(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    firstLastName: Optional[str] = None
    secondLastName: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    neighborhood: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    identification: Optional[str] = None
    id: Optional[str]


class AuthParams(BaseModel):
    email: str
    password: str


class CarParams(BaseModel):
    user: str
    brand: str
    color: str
    model: str
    km: str
    plate: str
    year: int
    transmission: str
    extras: Optional[str] = None
    photos: Optional[list]


class TokenParams(BaseModel):
    access_token: str
    token_type: str