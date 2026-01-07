from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base      

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True) 

    # relationship 1-n with Books
    # back_populates trỏ về tên biến 'category' bên trong class Book
    books = relationship("Book", back_populates="category")