from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from .models import Worker, Workstation, AIEvent

def seed_data(db: Session):
    db.query(AIEvent).delete()
    db.query(Worker).delete()
    db.query(Workstation).delete()

    workers = [Worker(id=f"W{i}", name=f"Worker {i}") for i in range(1, 7)]
    stations = [Workstation(id=f"S{i}", name=f"Station {i}") for i in range(1, 7)]

    db.add_all(workers + stations)

    now = datetime.utcnow()
    events = []

    for i in range(6):
        for h in range(8):
            events.append(
                AIEvent(
                    timestamp=now - timedelta(hours=h),
                    worker_id=f"W{i+1}",
                    workstation_id=f"S{i+1}",
                    event_type="working",
                    confidence=0.95,
                    count=1
                )
            )

    db.add_all(events)
    db.commit()
