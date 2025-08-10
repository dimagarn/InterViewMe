from sqlalchemy import Column, Integer, String, Text, JSON, column
from database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    typical_phrases = Column(JSON, nullable=False)
    advice_tips = Column(JSON, nullable=False)
    revenge_tactics = Column(JSON, nullable=False)
    avatar_url = Column(String(255), nullable=True)