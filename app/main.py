from app.database import engine
from app.models import Base
from fastapi import FastAPI

from sqlalchemy.orm import Session
from fastapi import Depends

from app.schemas import EventCreate
from app.models import Event
from app.database import get_db

from app.models import Event
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi import Depends

app = FastAPI(
    title="Store Intelligence API",
    version="1.0"
)
Base.metadata.create_all(bind=engine)

@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()

@app.get("/")
def home():
    return {
        "message": "Store Intelligence API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/events/ingest")
def ingest_event(
    event: EventCreate,
    db: Session = Depends(get_db)
):
    new_event = Event(
        event_id=event.event_id,
        store_id=event.store_id,
        visitor_id=event.visitor_id,
        event_type=event.event_type,
        timestamp=event.timestamp,
        zone_id=event.zone_id,
        confidence=event.confidence,
        is_staff=event.is_staff
    )

    db.add(new_event)
    db.commit()

    return {
        "message": "Event stored successfully"
    }

@app.get("/analytics")
def analytics(db: Session = Depends(get_db)):
    events = db.query(Event).all()

    entries = len([
        e for e in events
        if e.event_type == "entry"
    ])

    zones = len([
        e for e in events
        if e.event_type == "zone_entered"
    ])

    billing = len([
        e for e in events
        if e.event_type == "queue_completed"
    ])

    return {
        "total_events": len(events),
        "entries": entries,
        "zone_events": zones,
        "billing_events": billing,
        "stores_monitored": len(
            set(e.store_id for e in events)
        )
    }