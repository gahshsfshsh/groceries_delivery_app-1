import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()

POSTGRES_URL = os.environ.get("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/groceries")

# SQLAlchemy engine
engine = create_engine(POSTGRES_URL)

# Базовый класс моделей
Base = declarative_base()

# Локальная сессия для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
      db = SessionLocal()
      try:
                yield db
finally:
        db.close()
  
