from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    app_name: str = "HackSeek API"
    app_version: str = "1.0.0"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    
   
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./hackseek.db")
    
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # CORS Configuration
    cors_origins: list = [
        "http://localhost:3000",
        "http://localhost:3001", 
        "https://your-frontend-domain.com"  # Add your actual frontend URL
    ]
    
   
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    class Config:
        env_file = "../../.env"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

settings = Settings()