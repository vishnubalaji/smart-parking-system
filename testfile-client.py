import firebase_admin
from firebase_admin import credentials, firestore
import threading, time
# Create an Event for notifying main thread.
# callback_done = threading.Event()

# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f'Received document snapshot: {doc.id}')
    # callback_done.set()

cred = credentials.Certificate("firestore-fastapi-firebase-adminsdk-w5pg4-e2c5f699b2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'smart-parking-sensors').document(u'sensors-19:40')

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)
while True:
    time.sleep(1)
    print("Listening for updations...\n")