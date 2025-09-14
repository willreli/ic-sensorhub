from pydantic import BaseModel
from datetime import datetime

class DeviceCreate(BaseModel):
    name: str

class SensorReadingCreate(BaseModel):
    device_id: int
    metric: str
    value: float
    timestamp: datetime

class SensorReading(SensorReadingCreate):
    id: int

    class Config:
        orm_mode = True

class Device(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

