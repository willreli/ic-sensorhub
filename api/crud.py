from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from sqlalchemy import distinct

def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(name=device.name)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def create_readings(db: Session, readings: list[schemas.SensorReadingCreate]):
    db_readings = [
        models.SensorReading(**reading.dict()) for reading in readings
    ]
    db.add_all(db_readings)
    db.commit()
    return {"inserted": len(db_readings)}

def get_readings(db: Session, device_id: int, metric: str, start: str, end: str, limit: int = 100):
    return (
        db.query(models.SensorReading)
        .filter(models.SensorReading.device_id == device_id)
        .filter(models.SensorReading.metric == metric)
        .filter(models.SensorReading.timestamp >= start)
        .filter(models.SensorReading.timestamp <= end)
        .order_by(models.SensorReading.timestamp)
        .limit(limit)
        .all()
    )

def get_all_devices(db: Session):
    return db.query(models.Device).all()

def get_metrics_for_device(db: Session, device_id: int):
    return db.query(distinct(models.SensorReading.metric)) \
             .filter(models.SensorReading.device_id == device_id) \
             .all()

