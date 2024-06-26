from sqlalchemy import Column, Integer, String

from src.database.database import Base


class About(Base):
    __tablename__ = "about"

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(length=60), nullable=False)
    content: str = Column(String(length=30000), nullable=False)
