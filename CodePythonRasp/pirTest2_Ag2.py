#!/usr/bin/python
import RPi.GPIO as GPIO
import time

import paho.mqtt.client as mqtt

def on_connect(client, userdata,flag,rc):
    print("CapteurHumid Connected")

client = mqtt.Client(client_id="CapteurPres2")
ip= '192.168.43.37'
#ip= '10.60.160.97'
#ip= '10.188.109.197'
PORT=1883

client.on_connect = on_connect
client.connect(ip,PORT,60)
client.loop_start()

SENSOR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN,GPIO.IN)

def my_callback(channel):
        print("Something moved !")
        t=time.localtime()
        x = t[5] + t[4]*60 + t[3]*3600
        #publish actual time in seconds
        client.publish("/Agregat2/pres",x)
        
try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(2)
        print("alive")
        
except KeyboardInterrupt:
    print("Finish")
GPIO.cleanup()