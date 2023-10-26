from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr, validator


class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str

    
class UserSchema(CreateUserSchema):
    full_name: str
    address: str
    _id: int


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str 


class TokenSchema(BaseModel):
    Authorization: str
