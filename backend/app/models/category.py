import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, constr, HttpUrl

Base = declarative_base()

# SQLAlchemy модель категории (PostgreSQL)
class Category(Base):
      __tablename__ = "categories"
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
      name = Column(String(128), nullable=False)
      image_url = Column(String(250), nullable=True)

# Pydantic схемы
class CategoryBase(BaseModel):
      name: constr(min_length=1, max_length=128)
      image_url: HttpUrl | None = None

class CategoryCreate(CategoryBase):
      pass

class CategoryRead(CategoryBase):
      id: uuid.UUID

    class Config:
              orm_mode = True
      
