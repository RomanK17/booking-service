from fastapi import HTTPException, status

UserAlredyExistsException = HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Пользователь с такими данными уже есть в базе данных')

UserNotRegisteredException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Пользователя с таким email или паролем не существует!')