from fastapi import APIRouter, HTTPException, Response, status
from .schemas import SchemaUserAuth
from .service import UserService
from .auth import create_access_token, get_password_hash, verify_password, authenticate_user
router = APIRouter(prefix='/auth', tags=['Пользователи'])

@router.post('/register')
async def register_user(user_data: SchemaUserAuth):
    existing_user = await UserService.find_one_or_none(email=user_data.email) 
    if existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пользователь с таким email уже существует')
    hashed_password = get_password_hash(user_data.password)
    await UserService.insert_data(email=user_data.email, hashed_password=hashed_password)
    
@router.post('/auth')
async def auth_user(response: Response, user_data: SchemaUserAuth):
    existing_user = await authenticate_user(email=user_data.email, password=user_data.password)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пользователя с таким email или паролем не существует!')
    access_token = create_access_token({'sub': str(existing_user.id)})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return access_token