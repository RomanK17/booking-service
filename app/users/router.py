from fastapi import APIRouter, HTTPException
from .schemas import SchemaUserRegister
from .service import UserService
from .auth import get_password_hash, verify_password
router = APIRouter(prefix='/auth', tags=['Пользователи'])

@router.post('/register')
async def register_user(user_data: SchemaUserRegister):
    existing_user = await UserService.find_one_or_none(email=user_data.email) 
    if existing_user:
        raise HTTPException(status_code=401)
    hashed_password = get_password_hash(user_data.password)
    await UserService.insert_data(email=user_data.email, hashed_password=hashed_password)