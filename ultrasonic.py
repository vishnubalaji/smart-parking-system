import RPi.GPIO as GPIO
import requests
import time
from datetime import datetime as dt

URL = 'https://smart-parking-system-fastapi.herokuapp.com/sensors/update'
{
	"date" : "03/15/22",
	"local_time":"22:14:32",
	"sensors" : {
		"sensor_1":"available",
		"sensor_2":"parked"
	}
}
TRIG=23
ECHO=24

GPIO.setmode(GPIO.BCM) # To follow broadcom chip-specific pin numbers

# Declaring pin mode, if it is an input or an output pin
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
    # To set TRIG pin as low
    GPIO.output(TRIG,False)
    time.sleep(0.2)
    # To set TRIG pin as high
    GPIO.output(TRIG,True)
    time.sleep(0.00001)

    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17200       # Speed = 344 m/s or 34400 cm/s. Since the distance is covered twice, half the time taken
    # distance=round(distance,2)
    
    if(distance < 5):        
        date = dt.now().strftime("%x")
        local_time = dt.now().strftime("%X")
        sensors = {
            "sensor_1":"parked"
        }

        body = {
            "date" : date,
            "local_time" : local_time,
            "sensors":sensors
        }
        requests.post(URL, json=body)
    time.sleep(2)