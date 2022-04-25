"""
To be run on Raspberry Pi 3
"""
import RPi.GPIO as GPIO
import requests
import time
import threading as th
# from datetime import datetime as dt

sensors = None
sensor1_stat = None
sensor2_stat = None

def sensor_1():
    GPIO.output(TRIG_1,False)
    time.sleep(0.2)
    GPIO.output(TRIG_1,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_1,False)

    while GPIO.input(ECHO_1)==0:
        pulse_start=time.time()
        
    while GPIO.input(ECHO_1)==1:
        pulse_end=time.time()
        
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17200       # Speed = 344 m/s or 34400 cm/s. Since the distance is covered twice, half the time taken
    # distance=round(distance,2)
    
    if(distance <= 5):
        # date = dt.now().strftime("%x")
        # local_time = dt.now().strftime("%X")
        sensor1_stat = "parked"
    else:
        sensor1_stat = "available"

def sensor_2():
    GPIO.output(TRIG_2,False)
    time.sleep(0.2)    
    GPIO.output(TRIG_2,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_2,False)

    while GPIO.input(ECHO_2)==0:
        pulse_start=time.time()
    
    while GPIO.input(ECHO_2)==1:
        pulse_end=time.time()
    
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17200       # Speed = 344 m/s or 34400 cm/s. Since the distance is covered twice, half the time taken
    # distance=round(distance,2)
    
    if(distance <= 5):
        # date = dt.now().strftime("%x")
        # local_time = dt.now().strftime("%X")
        sensor2_stat = "parked"
    else:
        sensor2_stat = "available"

if __name__ == "__main__":
    URL = 'https://smart-parking-system-fastapi.herokuapp.com/sensors/update'

    TRIG_1 = 18
    ECHO_1 = 23

    TRIG_2 = 24
    ECHO_2 = 25

    GPIO.setmode(GPIO.BCM) # To follow broadcom chip-specific pin numbers

    # Declaration of pin modes
    GPIO.setup(TRIG_1,GPIO.OUT)
    GPIO.setup(ECHO_1,GPIO.IN)

    GPIO.setup(TRIG_2,GPIO.OUT)
    GPIO.setup(ECHO_2,GPIO.IN)

    while True:
        # sensor1 = th.Thread(target=sensor_1())
        # sensor2 = th.Thread(target=sensor_2())
        
        # sensor1.start()
        # sensor2.start()

        sensor_1()
        sensor_2()

        sensors = {
            "sensor_1":sensor1_stat,
            "sensor_2":sensor2_stat
        }
        body = {
            # "date" : date,
            # "local_time" : local_time,
            "sensors":sensors
        }
        requests.post(URL, json=body)

        time.sleep(2)