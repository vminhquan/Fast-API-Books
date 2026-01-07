from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base      # <-- Import từ base_class

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=False)

    # Khóa ngoại trỏ đến bảng 'authors' và 'categories'
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="RESTRICT"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False)

    cover_image = Column(String(255), nullable=False)

    create_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    update_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # --- SỬA LẠI ĐOẠN NÀY ---
    # Biến này đại diện cho 1 tác giả (số ít)
    author = relationship("Author", back_populates="books")
    
    # Biến này đại diện cho 1 thể loại (số ít)
    category = relationship("Category", back_populates="books")