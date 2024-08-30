"""функции, которые используются в роутерах для получения данных для конкретного пользователя"""

from datetime import datetime
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, Request, status
from typing import Optional


from app.config import settings
from app.users.service import UserService
from app.users.models import Users

def get_jwt_token(request: Request) -> Optional[str]:
    token = request.cookies.get('booking_access_token')
    if token:
        return token
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Вы не авторизованы!')
    

async def get_current_user_id(token: str = Depends(get_jwt_token)) -> Users:
        try:
            res = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITM)
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Невалидный jwt токен')
        expire_time : str = res.get('exp_time')
        if not expire_time or datetime.fromisoformat(expire_time).timestamp() < datetime.now().timestamp():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Время действия jwt токена истекло')
        user_id : str = res.get('sub')
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='нет id пользователя')
        user = await UserService.find_by_id(int(user_id))
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'пользователя с id {user_id} не существует в базе данных')
        return user # TODO: почему возвращается юзер, а не id?

