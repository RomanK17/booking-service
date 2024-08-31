from fastapi import APIRouter, Depends, Response

from app.exceptions import UserAlredyExistsException, UserNotRegisteredException
from .schemas import SchemaUserAuth
from .service import UserService
from .auth import create_access_token, get_password_hash, verify_password, authenticate_user
from .dependencies import get_current_user_id


router = APIRouter(prefix='/auth', tags=['Users'])

@router.post('/register')
async def register_user(user_data: SchemaUserAuth):
    existing_user = await UserService.find_one_or_none(email=user_data.email) 
    if existing_user:
        raise UserAlredyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserService.insert_data(email=user_data.email, hashed_password=hashed_password)
    
@router.post('/auth')
async def auth_user(response: Response, user_data: SchemaUserAuth):
    existing_user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not existing_user:
        raise UserNotRegisteredException
    access_token = create_access_token({'sub': str(existing_user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return access_token

@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')
    return 'Вы успешно вышли из системы.'

@router.get('/current_user')
async def get_current_user(current_user_id: int = Depends(get_current_user_id)):
    return current_user_id