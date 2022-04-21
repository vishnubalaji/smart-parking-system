from datetime import datetime as dt
import string
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class sensors(BaseModel):
    sensor_1:str
    sensor_2:str

class UltrasonicSensors(BaseModel):
    date : str
    local_time : str    # In IST
    sensors : sensors

app = FastAPI()
cred = credentials.Certificate("firestore-fastapi-firebase-adminsdk-w5pg4-e2c5f699b2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.post("/sensors/update")
def sensor_status(sensors: UltrasonicSensors):
    json_data = jsonable_encoder(sensors)
    doc_ref = db.collection(u'smart-parking-sensors').document(u'sensors-status')
    doc_ref.set({
        u'date': json_data['date'],
        u'local_time': json_data['local_time'],
        u'sensors': {
            u'sensor_1' : json_data['sensors']['sensor_1'],
            u'sensor_2': json_data['sensors']['sensor_2']
        }
    })
    return "Updation is successful"
    # print(f'---{sensors}---\n---API is working fine---')
    # return sensors

@app.get("/sensors/retrieve")
def sensor_status_frontend():
    return "Database is under construction. Apologies for the inconvenience."