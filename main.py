#from Hardware import controller
# -*- coding: utf-8 -*-
import threading
from flask import Flask, render_template, request, jsonify
import datetime
import HCSR04
import Servo
import System
import run


etat_porte = ""

app = Flask(__name__)

@app.route('/',)
def DataEntry():
    global cptr_items
    etat_porte = "Ferme"
    now = datetime.datetime.now()
    time_porte = now.strftime("%Y-%m-%d %H:%M")
    return render_template('index.html', time_porte=time_porte, etat_porte=etat_porte, items=HCSR04.cptr_items)

@app.route('/get_item_count', methods=['GET'])
def get_item_count():
    global cptr_items
    item_count = HCSR04.cptr_items
    return jsonify({'items': item_count})

@app.route('/result',methods = ['POST', 'GET'])
def result():

    global etat_porte
    print("Etat porte: ",request.form.get('porte'))

    if request.form.get('porte') == "Porte_entrant":
        print("Porte entrante ouverte")
        etat_porte = 'Ouverte'
        HCSR04.Door_open_In()
        Servo.OpenDoor(90)

    elif request.form.get('porte') == "Porte_sortant":
        print("Porte sortante ouverte")
        etat_porte = 'Ouverte'
        HCSR04.Door_open_Out()
        Servo.OpenDoor(90)

    else:
        print("Aucune porte selectionnee")
        etat_porte = 'Aucune porte selectionnee'    

    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'etat': etat_porte
      } 
    return render_template('result.html', **templateData)

if __name__ == '__main__':
    trig_pin_interieur = 21
    echo_pin_interieur = 20
    trig_pin_exterieur = 19
    echo_pin_exterieur = 16
    HCSR04.initialiser_capteurs(trig_pin_interieur, echo_pin_interieur, trig_pin_exterieur, echo_pin_exterieur)

    # Créez un thread pour mettre à jour le compteur d'items en arrière-plan
    update_thread = threading.Thread(target=HCSR04.update_item_counter)
    update_thread.daemon = True
    update_thread.start()

    threadManageDoor = run.ManageDoor()
    threadGate = run.ManageGate()
    threadInsideSensor = threading.Thread(target=HCSR04.gestion_capteur_interieur, args=(trig_pin_interieur, echo_pin_interieur))
    threadOutsideSensor = threading.Thread(target=HCSR04.gestion_capteur_exterieur, args=(trig_pin_exterieur, echo_pin_exterieur))
    
    threadManageDoor.start() 
    threadGate.start()
    threadInsideSensor.start()
    threadOutsideSensor.start()

    app.run(debug=True, host='0.0.0.0') 