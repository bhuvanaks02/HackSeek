from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class Hackathon(Base):
    __tablename__ = "hackathons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text)
    url = Column(String, nullable=False)
    source = Column(String, nullable=False)  # e.g., "devpost", "eventbrite"
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    deadline = Column(DateTime)
    location = Column(String)
    is_virtual = Column(Boolean, default=False)
    prizes = Column(JSON)  # Store prize information as JSON
    tags = Column(JSON)    # Store tags/categories as JSON array
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())