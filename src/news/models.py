from datetime import datetime
from fastapi_storages import FileSystemStorage
from sqlalchemy import Column, String, ForeignKey, Integer, Date, ARRAY
from sqlalchemy.orm import relationship
from fastapi_storages.integrations.sqlalchemy import FileType

from src.database.database import Base

storage = FileSystemStorage(path="static/media/news")


class NewsCategory(Base):
    __tablename__ = "news_category"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), nullable=False)

    news = relationship("News", back_populates="category")

    def __repr__(self) -> str:
        return f"{self.name}"


class News(Base):
    __tablename__ = "news"

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(60), nullable=False)
    content: str = Column(String(30000), nullable=False)
    short_description: str = Column(String(200), nullable=False)
    authors: list[str] = Column(ARRAY(String(25)), nullable=False)
    editors: list[str] = Column(ARRAY(String(25)))
    photographers: list[str] = Column(ARRAY(String(25)))
    preview_photo: str = Column(FileType(storage=storage), nullable=False)
    created_at: datetime = Column(Date(), nullable=False)
    category_id: int = Column(Integer, ForeignKey("news_category.id"))
    city_id = Column(Integer, ForeignKey("cities.id"))

    category = relationship("NewsCategory", back_populates="news", lazy="selectin")
    location = relationship("City", back_populates="news", lazy="selectin")

    def __repr__(self) -> str:
        return f"{self.title}"
