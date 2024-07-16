from fastapi import HTTPException, status

class BookingException(HTTPException):
    detail = ""
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
        

class UserAlredyExistsException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail='Пользователь с такими данными уже есть в базе данных'
    
    
class UserNotRegisteredException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Пользователя с таким email или паролем не существует!'
    