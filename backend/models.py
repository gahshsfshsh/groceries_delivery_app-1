import uuid
from datetime import datetime
from enum import Enum
from sqlalchemy import (
    Column, String, Text, Integer, Float, DECIMAL, ForeignKey, Enum as PgEnum,
    DateTime
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class OrderStatus(str, Enum):
      CREATED = "created"
      PROCESSING = "processing"
      DELIVERED = "delivered"
      CANCELED = "canceled"

class User(Base):
      __tablename__ = "users"
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
      phone_number = Column(String(64), unique=True, nullable=False, index=True)
      created_at = Column(DateTime, default=datetime.utcnow)
      updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
      orders = relationship("Order", back_populates="user")

class Category(Base):
      __tablename__ = "categories"
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
      name = Column(String(128), nullable=False)
      image_url = Column(String(512), nullable=True)
      products = relationship("Product", back_populates="category")

class Product(Base):
      __tablename__ = "products"
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
      category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))
      name = Column(String(256), nullable=False)
      description = Column(Text, nullable=False)
      image_url = Column(String(512), nullable=False)
      price = Column(DECIMAL(10, 2), nullable=False)
      discount_price = Column(DECIMAL(10, 2), nullable=True)
      stock = Column(Integer, nullable=False, default=0)
      rating = Column(Float, nullable=True)
      composition = Column(Text, nullable=True)
      nutritional_value = Column(Text, nullable=True)
      calories = Column(Integer, nullable=True)
      weight = Column(Float, nullable=True)
      country = Column(String(128), nullable=True)
      category = relationship("Category", back_populates="products")
      order_items = relationship("OrderItem", back_populates="product")

class Order(Base):
      __tablename__ = "orders"
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
      user_phone = Column(String(64), nullable=False)
      user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
      delivery_address = Column(Text, nullable=False)
      delivery_time = Column(DateTime, nullable=True)
      total_price = Column(DECIMAL(10, 2), nullable=False)
      status = Column(PgEnum(OrderStatus, name="order_status"), default=OrderStatus.CREATED)
      created_at = Column(DateTime, default=datetime.utcnow)
      updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
      __tablename__ = "order_items"
      id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
      order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"))
      product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
      quantity = Column(Integer, nullable=False)
      price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
