from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str 
    DB_PORT: int 
    DB_USER: str 
    DB_PASSWORD: str 
    DB_NAME: str
    ALGORITM: str
    SECRET_KEY: str
    
    class Config:
        env_file = '.env'
        
settings = Settings()
DB_URL = f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'