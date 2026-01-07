from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base  # <-- Import từ base_class


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=False)

    # Khóa ngoại trỏ đến bảng 'authors' và 'categories'
    author_id = Column(
        Integer, ForeignKey("authors.id", ondelete="RESTRICT"), nullable=False
    )
    category_id = Column(
        Integer, ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False
    )

    cover_image = Column(String(255), nullable=False)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    author = relationship("Author", back_populates="books")

    category = relationship("Category", back_populates="books")
