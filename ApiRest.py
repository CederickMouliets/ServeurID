import time

from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

#http://192.168.43.37:5000/api/bureau/
#http://192.168.43.37:5000/api/foyer/

t1 = time.localtime()[4]
t2 = time.localtime()[4]

dico1 = None
dico2 = None


@app.route('/api/foyer/')
def foyer():
    global t1, dico1
    f1 = open("Agregat1_temp.txt", "r")
    f2 = open("Agregat1_pres.txt", "r")
    f3 = open("Agregat1_humid.txt", "r")

    current_time = time.localtime()

    #update every minutes
    if current_time[4] - t1 != 0 or dico1 is None:
        dictionnaire = {
            'Temperature': f1.read(),
            'Humidity': f3.read(),
            'Time last Move': f2.read()
        }
        dico1 = dictionnaire;
        t1=current_time[4];

    f1.close()
    f2.close()
    f3.close()

    return json.dumps(dico1)

@app.route('/api/bureau/')
def bureau():
    global t2, dico2
    f1 = open("Agregat2_temp.txt", "r")
    f2 = open("Agregat2_pres.txt", "r")
    f3 = open("Agregat2_humid.txt", "r")

    current_time = time.localtime()

    #update every minutes
    if current_time[4] - t2 != 0 or dico2 is None:
        dictionnaire = {
            'Temperature': f1.read(),
            'Humidity': f3.read(),
            'Time last Move': f2.read()
        }

        dico2 = dictionnaire;
        t2=current_time[4];

    f1.close()
    f2.close()
    f3.close()

    return json.dumps(dico2)


if __name__ == "__main__":
    #l'appel de API REST est bloquant, on le lance dans un autre script
    #app.run(host="192.168.43.37")
    #app.run(host="10.60.160.97")
    app.run(host="10.188.109.197")
 