from uuid import uuid4
import bcrypt
import jwt
from config.settings import get_settings
from db.mongo import db

jwt_collection = db['token']


async def hash_password(password) -> str:
    """Transforms password from it's raw textual form to 
    cryptographic hashes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


async def check_password(password: str, hashed_password: str) -> bool:
    """Checks if a password matches a hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password)


async def gen_jti():
    return uuid4().hex


async def generate_token(user) -> dict:
    """Generate access token for user"""
    jti = await gen_jti(

    )

    await jwt_collection.insert_one({f'jti': user['_id']})

    tokens = {
        "access_token": jwt.encode(
            {'type': 'access', "email": user['email'], 'jti': jti},
            get_settings().secret_key
        ),
        "refresh_token": jwt.encode(
            {'type': 'refresh', "email": user['email'], 'jti': jti},
            get_settings().secret_key
        )
    }
    return tokens
