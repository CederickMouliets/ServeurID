import time
import paho.mqtt.client as mqtt

#http://192.168.43.37:5000/api/bureau/
#http://192.168.43.37:5000/api/foyer/

#connexion capteur presence
#5V  = 2eme broche
#res = GPIO 4 (7eme broche)
#gnd = 6eme broche

#connexion capteur humidite
#3.3V  = 17eme broche
#res   = GPIO 24 (18eme broche)
#gnd   = 14eme broche

#'localhost'
#'10.188.109.197'
#'192.168.43.37'
class Serveur:
    def __init__(self, ip='192.168.43.37', port=1883, id='0'):
        self.id = id
        
        self.client = mqtt.Client(client_id="Serveur"+id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(ip, port=port)
        self.client.subscribe("/Agregat1/temp")
        self.client.subscribe("/Agregat1/humid")
        self.client.subscribe("/Agregat1/pres")

        self.client.subscribe("/Agregat2/temp")
        self.client.subscribe("/Agregat2/humid")
        self.client.subscribe("/Agregat2/pres")
        self.client.loop_start()
        

    # Action lorsque le serveur c'est bien connecté au réseau MQTT
    def on_connect(self, client, userdata, flag, rc):
        print("Serveur" + self.id + " connecte !")

    def on_message(self, client, userdata, msg):
        x = None
        try :
            x = str(msg.payload.decode("utf-8"))
        except :
            x = None

        print("new message: " + msg.topic + " - " + x)

        if(msg.topic=="/Agregat1/temp"):
                f = open("Agregat1_temp.txt", "w")
        elif(msg.topic=="/Agregat1/humid"):
                f = open("Agregat1_humid.txt", "w")
        elif(msg.topic=="/Agregat1/pres"):
                f = open("Agregat1_pres.txt", "w")
        elif(msg.topic=="/Agregat2/temp"):
                f = open("Agregat2_temp.txt", "w")
        elif(msg.topic=="/Agregat2/humid"):
                f = open("Agregat2_humid.txt", "w")
        else: #(msg.topic=="Agregat2/pres")
                f = open("Agregat2_pres.txt", "w")

        print("on écrit\n")
        f.write(x)
        f.close()


    def send_on(self):
        self.client.publish("/serveur"+self.id+"/online", "ON")

if __name__ == "__main__":

    c = Serveur()
    # Envoie d'une donnée pour dire que le serveur est en vie
    while(True) :
        c.send_on()
        time.sleep(1)