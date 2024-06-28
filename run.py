import time
import threading
import RPi.GPIO as GPIO

# Configuration des broches pour les moteurs servo de la porte et de la barrière
servo_pin_porte = 18  # Changer le numéro de broche GPIO en fonction de votre configuration
servo_pin_barriere = 19  # Changer le numéro de broche GPIO en fonction de votre configuration

# Configuration initiale
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_porte, GPIO.OUT)
GPIO.setup(servo_pin_barriere, GPIO.OUT)

# Création d'un objet PWM pour le moteur servo de la porte
pwm_porte = GPIO.PWM(servo_pin_porte, 50)  # Fréquence de PWM de 50 Hz (peut être ajustée)

# Création d'un objet PWM pour le moteur servo de la barrière
pwm_barriere = GPIO.PWM(servo_pin_barriere, 50)  # Fréquence de PWM de 50 Hz (peut être ajustée)

# Fonction pour ouvrir la porte
def ouvrir_porte():
    pwm_porte.start(0)  # Démarrer le signal PWM avec un rapport cyclique de 0 (porte fermée)
    # Calculer le rapport cyclique pour ouvrir la porte (à ajuster en fonction de votre servo)
    duty_cycle = (angle_ouverture_porte / 18.0) + 2.5
    pwm_porte.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre à la porte de s'ouvrir
    pwm_porte.ChangeDutyCycle(0)  # Arrêter le signal PWM

# Fonction pour fermer la porte
def fermer_porte():
    pwm_porte.start(0)  # Démarrer le signal PWM avec un rapport cyclique de 0 (porte ouverte)
    # Calculer le rapport cyclique pour fermer la porte (à ajuster en fonction de votre servo)
    duty_cycle = (angle_fermeture_porte / 18.0) + 2.5
    pwm_porte.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre à la porte de se fermer
    pwm_porte.ChangeDutyCycle(0)  # Arrêter le signal PWM

# Fonction pour ouvrir la barrière
def ouvrir_barriere():
    pwm_barriere.start(0)  # Démarrer le signal PWM avec un rapport cyclique de 0 (barrière fermée)
    # Calculer le rapport cyclique pour ouvrir la barrière (à ajuster en fonction de votre servo)
    duty_cycle = (angle_ouverture_barriere / 18.0) + 2.5
    pwm_barriere.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre à la barrière de s'ouvrir
    pwm_barriere.ChangeDutyCycle(0)  # Arrêter le signal PWM

# Fonction pour fermer la barrière
def fermer_barriere():
    pwm_barriere.start(0)  # Démarrer le signal PWM avec un rapport cyclique de 0 (barrière ouverte)
    # Calculer le rapport cyclique pour fermer la barrière (à ajuster en fonction de votre servo)
    duty_cycle = (angle_fermeture_barriere / 18.0) + 2.5
    pwm_barriere.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre à la barrière de se fermer
    pwm_barriere.ChangeDutyCycle(0)  # Arrêter le signal PWM

# Définir une classe pour gérer la porte
class ManageDoor(threading.Thread):
    def __init__(self):
        super(ManageDoor, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            # Insérez ici la logique de gestion de la porte
            etat_porte = 'Ouverte'  # Par exemple, obtenez cet état à partir de vos capteurs
            if etat_porte == 'Ouverte':
                fermer_porte()  # Si la porte est ouverte, fermez-la
            elif etat_porte == 'Fermee':
                ouvrir_porte()  # Si la porte est fermée, ouvrez-la
            time.sleep(1)

# Définir une classe pour gérer la barrière
class ManageGate(threading.Thread):
    def __init__(self):
        super(ManageGate, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            # Insérez ici la logique de gestion de la barrière
            etat_barriere = 'Ouverte'  # Par exemple, obtenez cet état à partir de vos capteurs
            if etat_barriere == 'Ouverte':
                fermer_barriere()  # Si la barrière est ouverte, fermez-la
            elif etat_barriere == 'Fermee':
                ouvrir_barriere()  # Si la barrière est fermée, ouvrez-la
            time.sleep(1)

# Arrêter proprement les moteurs servo lorsque le programme se termine
def cleanup():
    pwm_porte.stop()
    pwm_barriere.stop()
    GPIO.cleanup()

# Configuration des angles d'ouverture et de fermeture pour la porte et la barrière
angle_ouverture_porte = 90  # À ajuster en fonction de votre servo de porte
angle_fermeture_porte = 0   # À ajuster en fonction de votre servo de porte

angle_ouverture_barriere = 90  # À ajuster en fonction de votre servo de barrière
angle_fermeture_barriere = 0   # À ajuster en fonction de votre servo de barrière
