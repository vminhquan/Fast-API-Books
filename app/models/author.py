from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship # Nhớ import từ orm
from app.db.base_class import Base      # <-- Import từ base_class

class Author(Base):
    __tablename__ = "authors"  # <-- Sửa thành số nhiều

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    bio = Column(Text, nullable=True)

    # relationship 1-n with Books
    # back_populates trỏ về tên biến 'author' bên trong class Book
    books = relationship("Book", back_populates="author") 