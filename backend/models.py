import uuid
from datetime import datetime
from enum import Enum
from typing import List, Optional
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, DateTime, Numeric, Enum as PgEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base
from pydantic import BaseModel

Base = declarative_base()

class OrderStatus(str, Enum):
      created = 'created'
      processing = 'processing'
      delivered = 'delivered'
      canceled = 'canceled'

class User(Base):
      __tablename__ = 'users'
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
      phone_number = Column(String, unique=True, nullable=False)
      created_at = Column(DateTime, default=datetime.utcnow)
      updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
      orders = relationship('Order', back_populates='user')

class Category(Base):
      __tablename__ = 'categories'
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
      name = Column(String, nullable=False)
      image_url = Column(String)
      products = relationship('Product', back_populates='category')

class Product(Base):
      __tablename__ = 'products'
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
      category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=False)
      name = Column(String, nullable=False)
      description = Column(Text)
      image_url = Column(String)
      price = Column(Numeric(10, 2), nullable=False)
      discount_price = Column(Numeric(10, 2))
      stock = Column(Integer)
      rating = Column(Float)
      composition = Column(Text)
      nutritional_value = Column(Text)
      calories = Column(Integer)
      weight = Column(Float)
      country = Column(String)
      category = relationship('Category', back_populates='products')

class Order(Base):
      __tablename__ = 'orders'
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
      user_phone = Column(String)
      user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
      delivery_address = Column(Text)
      delivery_time = Column(DateTime)
      total_price = Column(Numeric(10,2), nullable=False)
      status = Column(PgEnum(OrderStatus), default=OrderStatus.created, nullable=False)
      created_at = Column(DateTime, default=datetime.utcnow)
      updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
      user = relationship('User', back_populates='orders')
      items = relationship('OrderItem', back_populates='order')

class OrderItem(Base):
      __tablename__ = 'order_items'
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
      order_id = Column(UUID(as_uuid=True), ForeignKey('orders.id'), nullable=False)
      product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'), nullable=False)
      quantity = Column(Integer, nullable=False)
      price = Column(Numeric(10,2), nullable=False)
      order = relationship('Order', back_populates='items')
      product = relationship('Product')

# ==== Pydantic Schemas ====

class CategoryBase(BaseModel):
      id: uuid.UUID
      name: str
      image_url: Optional[str]

    class Config:
              orm_mode = True

class ProductBase(BaseModel):
      id: uuid.UUID
      category_id: uuid.UUID
      name: str
      description: Optional[str]
      image_url: Optional[str]
      price: float
      discount_price: Optional[float]
      stock: Optional[int]
      rating: Optional[float]
      composition: Optional[str]
      nutritional_value: Optional[str]
      calories: Optional[int]
      weight: Optional[float]
      country: Optional[str]

    class Config:
              orm_mode = True

class OrderItemRead(BaseModel):
      id: uuid.UUID
      product_id: uuid.UUID
      quantity: int
      price: float

    class Config:
              orm_mode = True

class OrderRead(BaseModel):
      id: uuid.UUID
      user_phone: Optional[str]
      user_id: Optional[uuid.UUID]
      delivery_address: Optional[str]
      delivery_time: Optional[datetime]
      total_price: float
      status: OrderStatus
      created_at: datetime
      updated_at: datetime
      items: List[OrderItemRead] = []

    class Config:
              orm_mode = True

class UserRead(BaseModel):
      id: uuid.UUID
      phone_number: str
      created_at: datetime
      updated_at: datetime

    class Config:
              orm_mode = True
      
