from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import EmailStr
import jwt

from app.config import settings

from app.users.service import UserService

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def authenticate_user(email : EmailStr, password : str):
    user = await UserService.find_one_or_none(email=email) 
    if user and verify_password(password, user.hashed_password):
        return user
    else:
        return None

def create_access_token(data: dict)-> str:
    data_to_encode = data.copy()
    expire_time = (datetime.now() + timedelta(minutes=30)).isoformat()
    data_to_encode.update({'exp_time': expire_time})
    jwt_token= jwt.encode(data_to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITM)
    return jwt_token
    