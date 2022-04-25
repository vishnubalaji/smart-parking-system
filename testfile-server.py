from datetime import datetime as dt
from genericpath import exists
from heapq import merge
import string
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json

import firebase_admin
from firebase_admin import credentials, firestore

class sensors(BaseModel):
    sensor_1:str
    sensor_2:str

class UltrasonicSensors(BaseModel):
    # date : str
    # local_time : str    # In IST
    sensors : sensors

app = FastAPI()
cred = credentials.Certificate("firestore-fastapi-firebase-adminsdk-w5pg4-e2c5f699b2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.post("/sensors/update")
def sensor_status_firebase(sensors: UltrasonicSensors):
    json_data = jsonable_encoder(sensors)
    # sensor_time = json_data['local_time']
    doc_ref = db.collection(u'smart-parking-sensors').document(u'ultrasonic-sensors')
    data = {
        # u'date': json_data['date'],
        u'server-received-date':firestore.SERVER_TIMESTAMP,
        # u'local_time': json_data['local_time'],
        u'sensors': {
            u'sensor_1' : json_data['sensors']['sensor_1'],
            u'sensor_2': json_data['sensors']['sensor_2']
        }
    }
    # doc_ref.set(data,merge=True)
    doc_ref.set(data)
    return "Updation is successful"

@app.get("/sensors/retrieve")
def sensor_status_terminal():
    doc_ref = db.collection(u'smart-parking-sensors').document(u'ultrasonic-sensors')
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else 'Document doesn\'t exist :('

# Outdated format
"""
{
	"date" : "03/15/22",
	"local_time":"22:14:32",
	"sensors" : {
		"sensor_1":"available",
		"sensor_2":"available"
	}
}
"""

# Updated format
"""
{
	"sensors" : {
		"sensor_1":"available",
		"sensor_2":"available"
	}
}
"""