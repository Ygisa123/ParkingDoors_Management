# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import servo
import threading

def initialiser_capteurs(trig_pin_interieur, echo_pin_interieur, trig_pin_exterieur, echo_pin_exterieur):
    # Configuration du mode GPIO
    GPIO.setmode(GPIO.BCM)

    # Configuration des broches en entrée/sortie
    GPIO.setup(trig_pin_interieur, GPIO.OUT)
    GPIO.setup(echo_pin_interieur, GPIO.IN)

    GPIO.setup(trig_pin_exterieur, GPIO.OUT)
    GPIO.setup(echo_pin_exterieur, GPIO.IN)

def distance(trig_pin, echo_pin):
    # Code de mesure de la distance comme précédemment
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(echo_pin) == 0:
        StartTime = time.time()

    while GPIO.input(echo_pin) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

def gestion_capteur_exterieur(trig_pin_exterieur, echo_pin_exterieur):
    try:
        while True:
            # Mesurer la distance extérieure
            dist_exterieure = distance(trig_pin_exterieur, echo_pin_exterieur)
            print("Distance exterieure : %.2f cm" % dist_exterieure)
            # Si la distance est inférieure à une certaine valeur (objet détecté), ouvrir le moteur servo
            if dist_exterieure < 5:  # Vous pouvez ajuster cette valeur en fonction de votre besoin
                servo.OpenDoor(90)  # Ouvrir le moteur servo à un angle de 90 degrés
            
            time.sleep(1)

    except KeyboardInterrupt:
        print("Arret de la detection interieure.")


def gestion_capteur_interieur(trig_pin_interieur, echo_pin_interieur):
    try:
        while True:
            # Mesurer la distance intérieure
            dist_interieure = distance(trig_pin_interieur, echo_pin_interieur)
            print("Distance interieure : %.2f cm" % dist_interieure)
            
            # Si la distance est inférieure à une certaine valeur (objet détecté), ouvrir le moteur servo
            if dist_interieure < 5:  # Vous pouvez ajuster cette valeur en fonction de votre besoin
                servo.OpenDoor(90)  # Ouvrir le moteur servo à un angle de 90 degrés
            
            time.sleep(1)

    except KeyboardInterrupt:
        print("Arret de la detection interieure.")
