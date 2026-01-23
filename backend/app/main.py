from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, AIEvent
from .schemas import EventCreate
from .seed import seed_data

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Productivity Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root health check
@app.get("/")
def root():
    return {"status": "API is running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/events")
def ingest_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = AIEvent(**event.dict())
    db.add(db_event)
    db.commit()
    return {"status": "event ingested"}

@app.post("/seed")
def seed(db: Session = Depends(get_db)):
    seed_data(db)
    return {"status": "database seeded"}

@app.get("/metrics/workers")
def worker_metrics(db: Session = Depends(get_db)):
    events = db.query(AIEvent).all()
    metrics = {}

    for e in events:
        m = metrics.setdefault(e.worker_id, {
            "active_time": 0,
            "idle_time": 0,
            "units": 0
        })

        if e.event_type == "working":
            m["active_time"] += 1
        elif e.event_type == "idle":
            m["idle_time"] += 1

        if e.event_type == "product_count":
            m["units"] += e.count or 0

    for m in metrics.values():
        total = m["active_time"] + m["idle_time"]
        m["utilization"] = (m["active_time"] / total) * 100 if total else 0

    return metrics

@app.get("/metrics/factory")
def factory_metrics(db: Session = Depends(get_db)):
    events = db.query(AIEvent).all()
    productive = sum(1 for e in events if e.event_type == "working")
    units = sum(e.count or 0 for e in events)

    return {
        "total_productive_time": productive,
        "total_units": units,
        "avg_utilization": productive / max(len(events), 1)
    }

@app.get("/")
def root():
    return {
        "message": "AI Powered Worker Productivity Dashboard API is live",
        "docs": "/docs",
        "health": "OK"
    }
