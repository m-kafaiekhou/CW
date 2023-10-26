from typing import Dict
from fastapi import Body, FastAPI, Depends

from ..schemas.accounts_models import UserBaseSchema, UserLoginSchema, UserSchema, CreateUserSchema
from services.authentications import JWTBearer
from config.settings import app
from db.mongo import db
from db.db_func import *

user_collection = db['user']

@app.post('/login', response_model=Dict, dependencies=[Depends(JWTBearer())])
def login(
        payload: UserLoginSchema = Body(),
    ):

    try:
        get_one({'email': payload.email})
        
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    is_validated:bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    return user.generate_token()