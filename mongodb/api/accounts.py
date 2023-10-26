from typing import Dict
from fastapi import Body, Depends, HTTPException, Header, APIRouter

from schemas.accounts_models import *
from services.authentications import JWTBearer
from db.mongo import db
from db.db_func import *
from utils.utils import *

user_collection = db['user']

router = APIRouter()

@router.post('/login', response_model=Dict)
async def login(
        payload: UserLoginSchema,
    ):

    user = await get_one({'email': payload.email}, user_collection)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid user credentials"
        )
    
    is_validated:bool = await check_password(payload.password, user['password'])
    if not is_validated:
        raise HTTPException(
            status_code=401,
            detail="Invalid user credentials"
        )

    return await generate_token(user)


@router.post('/register', response_model=Dict)
async def register(
        payload: CreateUserSchema = Body(),
    ):

    
    user = await get_one({'email': payload.email}, user_collection)
    if user is not None:
        raise HTTPException(
            status_code=400,
            detail="email already exists"
        )
    
    _id = await user_collection.insert_one({'email': payload.email, 'password': await hash_password(payload.password)})

    return {'_id': str(_id.inserted_id)}


@router.get('/testauth')
async def testauth(token: bool = Depends(JWTBearer())):
    if not token:
        return {'message': ' Not Authenticated Ahmad Mohsen'}
    return {'message': 'Authenticated Ahmad Mohsen'}
