from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from .database import Base

class Worker(Base):
    __tablename__ = "workers"
    id = Column(String, primary_key=True)
    name = Column(String)

class Workstation(Base):
    __tablename__ = "workstations"
    id = Column(String, primary_key=True)
    name = Column(String)

class AIEvent(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    worker_id = Column(String, ForeignKey("workers.id"))
    workstation_id = Column(String, ForeignKey("workstations.id"))
    event_type = Column(String)
    confidence = Column(Float)
    count = Column(Integer, default=0)
