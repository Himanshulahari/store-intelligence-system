from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(String, unique=True)
    store_id = Column(String)

    visitor_id = Column(String)

    event_type = Column(String)

    timestamp = Column(String)

    zone_id = Column(String)

    confidence = Column(Float)

    is_staff = Column(Boolean, default=False)