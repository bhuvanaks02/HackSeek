from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from .config import settings

if settings.database_url.startswith("sqlite"):
  
    engine = create_engine(
        settings.database_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=settings.debug
    )
else:
    
    engine = create_engine(
        settings.database_url,
        echo=settings.debug,
        pool_pre_ping=True, 
        pool_recycle=300,   
    )


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()