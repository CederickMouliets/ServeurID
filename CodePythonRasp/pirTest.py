#!/usr/bin/python
import RPi.GPIO as GPIO
import time

SENSOR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN,GPIO.IN)

def my_callback(channel):
        print("Something moved !")
        t=time.localtime()
        x = t[5] + t[4]*60 + t[3]*3600
        #publish actual time in seconds
        print(x)
        
try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(2)
        print("alive")
        
except KeyboardInterrupt:
    print("Finish")
GPIO.cleanup()