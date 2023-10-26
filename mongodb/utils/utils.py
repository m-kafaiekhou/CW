import bcrypt
import jwt
from main import get_settings


def hash_password(password) -> str:
    """Transforms password from it's raw textual form to 
    cryptographic hashes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(password: str, hashed_password: str) -> bool:
    """Checks if a password matches a hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


def generate_token(user) -> dict:
        """Generate access token for user"""
        return {
            "access_token": jwt.encode(
                {"email": user.email},
                get_settings().secret_key
            )
        }
