
from pigpio_dht import DHT22
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata,flag,rc):
    print("CapteurHumid Connected")
    
client = mqtt.Client(client_id="CapteurHumid2")
ip= '192.168.43.37'
#ip= '10.60.160.97'
#ip= '10.188.109.197'
PORT=1883

client.on_connect = on_connect
client.connect(ip,PORT)
client.loop_start()

gpio = 24

sensor = DHT22(gpio)

try:
    while True:
        result = sensor.read()
        print(result)
        if (result["valid"]):
            client.publish("/Agregat2/temp",result["temp_c"])
            client.publish("/Agregat2/humid",result["humidity"])
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Finish")
