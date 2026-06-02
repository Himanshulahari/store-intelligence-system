from pydantic import BaseModel


class EventCreate(BaseModel):
    event_id: str
    store_id: str
    visitor_id: str
    event_type: str
    timestamp: str
    zone_id: str
    confidence: float
    is_staff: bool = False