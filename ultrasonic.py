import RPi.GPIO as GPIO
import requests
import time

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
    distance=pulse_duration*17150
    distance=round(distance,2)
    
    if(distance):
        pass
    time.sleep(2)