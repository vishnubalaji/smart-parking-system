from datetime import datetime as dt
import string
from fastapi import FastAPI
from pydantic import BaseModel

class sensors(BaseModel):
    sensor_1:str
    sensor_2:str

class UltrasonicSensors(BaseModel):
    date : str
    local_time : str    # In IST
    sensors : sensors


app = FastAPI()


@app.post("/sensors/update")
def sensor_status(sensors: UltrasonicSensors):
    print(f'---{sensors}---')
    return sensors

@app.get("/sensors/retrieve")
def sensor_status_frontend():
    return "Database is under construction. Apologies for the inconvenience."