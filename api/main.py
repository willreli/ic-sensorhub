from fastapi import FastAPI, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .deps import get_db, verify_api_key

import time
import logging
from sqlalchemy.exc import OperationalError
from .models import Base
from .deps import engine

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criar API FastAPI
app = FastAPI(title="Sensor API")

@app.post("/devices/", dependencies=[Depends(verify_api_key)])
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    return crud.create_device(db, device)

@app.get("/devices/", response_model=list[schemas.Device], dependencies=[Depends(verify_api_key)])
def list_devices(db: Session = Depends(get_db)):
    return crud.get_all_devices(db)

@app.post("/readings/", dependencies=[Depends(verify_api_key)])
def ingest_readings(readings: list[schemas.SensorReadingCreate], db: Session = Depends(get_db)):
    return crud.create_readings(db, readings)

@app.get("/readings/", response_model=list[schemas.SensorReading], dependencies=[Depends(verify_api_key)])
def get_readings(device_id: int, metric: str, start: str, end: str, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_readings(db, device_id, metric, start, end, limit)

@app.get("/metrics/", response_model=list[str], dependencies=[Depends(verify_api_key)])
def list_metrics(device_id: int, db: Session = Depends(get_db)):
    metrics = crud.get_metrics_for_device(db, device_id)
    return [m[0] for m in metrics]

# Tentar criar as tabelas aguardando banco estar pronto
MAX_TRIES = 10
for i in range(MAX_TRIES):
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Tabelas criadas com sucesso.")
        break
    except OperationalError as e:
        logger.warning(f"⏳ Tentando se conectar ao banco... tentativa {i+1}/{MAX_TRIES}")
        time.sleep(2)
else:
    logger.error("❌ Não foi possível conectar ao banco após várias tentativas.")

