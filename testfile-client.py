import firebase_admin
from firebase_admin import credentials, firestore
import threading, time
import requests
# Create an Event for notifying main thread.
# callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    # response = requests.get("http://127.0.0.1:8000/sensors/retrieve").json()
    response = requests.get("https://smart-parking-system-fastapi.herokuapp.com/sensors/retrieve").json()
    # print(response)
    print(f"Sensor-1 : {response['sensors']['sensor_1']}\tSensor-2 : {response['sensors']['sensor_2']}", end='\r')
    # for doc in doc_snapshot:
    #     print(f'Received document snapshot: {doc.id}', end = '\r')
    # callback_done.set()

cred = credentials.Certificate("firestore-fastapi-firebase-adminsdk-w5pg4-e2c5f699b2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'smart-parking-sensors').document(u'ultrasonic-sensors')

# print("Listening for changes in the document...\n")
# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)
while True:
    time.sleep(1)