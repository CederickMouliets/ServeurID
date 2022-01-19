Projet ID avec communication MQTT entre raspberry 3 et PC

Dans le dossier CodePythonRasp, il y a 6 scripts différents :

- DHT22Test.py : Test du capteur de température/humidité
- DHT22Test2.py : Envoie de données du capteur sur l'Agrégat1
- DHT22Test2_Ag2.py : Envoie de données du capteur sur l'Agrégat2

- pirTest.py : Test du capteur de présence
- pirTest2.py : Envoie de données du capteur sur l'Agrégat1
- pirTest2_Ag2.py : Envoie de données du capteur sur l'Agrégat2

Dans le dossier ServeurID, il y a l'interface Processing.

Le code ApiRest.py permet de lancer l'Api Rest du système.
Le code ServeurID.py lance le serveur qui souscrit aux publication des Agrégats.

Pour utiliser le système : il faudra lancer d'abord le démon pour que le capteur de température fonctionne : 

```
sudo pigpiod
```

Si la commande ne fonctionne pas, tuez tous les démons puis lancez en un :

```
sudo killall pigpiod
sudo pigpiod
```

Ensuite nous pouvons lancer les 4 Agrégats dans 4 terminaux :

```
python3 DHT22Test2.py
python3 pirTest2_.py
python3 pirTest2_Ag2.py
python3 DHT22Test2_Ag2.py
```

Dans le PC, il faut lancer l'application shiftr.io pour observer les requêtes MQTT passant par le système. Par ailleurs, les connexions internet du PC et des raspberry doivent être les mêmes. De plus, il faut récupérer l'adresse IPV4 du PC serveur et la recopier dans chaque création de client MQTT ainsi que dans l'API REST, sinon les connexions échouerons.

Ensuite, nous pouvons lancer les commandes dans deux terminaux différents du PC : 

```
python3 ServeurID.py
python3 ApiRest.py
```

Nous pouvons ensuite lancer l'interface graphique Processing ServeurID.pde.
Nous devrions pouvoir observer les bureaux du U3 ainsi que 2 cercles représentant les deux slots du systèmes.
