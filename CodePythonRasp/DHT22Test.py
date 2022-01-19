
from pigpio_dht import DHT22
import time

gpio = 24

sensor = DHT22(gpio)

try:
    while True:
        result = sensor.read()
        print(result)
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Finish")



