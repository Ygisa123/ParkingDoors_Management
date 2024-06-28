import time
import threading
import RPi.GPIO as GPIO

# Configuration des broches pour les moteurs servo de la porte et de la barri�re
servo_pin_porte = 18  # Changer le num�ro de broche GPIO en fonction de votre configuration
servo_pin_barriere = 19  # Changer le num�ro de broche GPIO en fonction de votre configuration

# Configuration initiale
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_porte, GPIO.OUT)
GPIO.setup(servo_pin_barriere, GPIO.OUT)

# Cr�ation d'un objet PWM pour le moteur servo de la porte
pwm_porte = GPIO.PWM(servo_pin_porte, 50)  # Fr�quence de PWM de 50 Hz (peut �tre ajust�e)

# Cr�ation d'un objet PWM pour le moteur servo de la barri�re
pwm_barriere = GPIO.PWM(servo_pin_barriere, 50)  # Fr�quence de PWM de 50 Hz (peut �tre ajust�e)

# Fonction pour ouvrir la porte
def ouvrir_porte():
    pwm_porte.start(0)  # D�marrer le signal PWM avec un rapport cyclique de 0 (porte ferm�e)
    # Calculer le rapport cyclique pour ouvrir la porte (� ajuster en fonction de votre servo)
    duty_cycle = (angle_ouverture_porte / 18.0) + 2.5
    pwm_porte.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre � la porte de s'ouvrir
    pwm_porte.ChangeDutyCycle(0)  # Arr�ter le signal PWM

# Fonction pour fermer la porte
def fermer_porte():
    pwm_porte.start(0)  # D�marrer le signal PWM avec un rapport cyclique de 0 (porte ouverte)
    # Calculer le rapport cyclique pour fermer la porte (� ajuster en fonction de votre servo)
    duty_cycle = (angle_fermeture_porte / 18.0) + 2.5
    pwm_porte.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre � la porte de se fermer
    pwm_porte.ChangeDutyCycle(0)  # Arr�ter le signal PWM

# Fonction pour ouvrir la barri�re
def ouvrir_barriere():
    pwm_barriere.start(0)  # D�marrer le signal PWM avec un rapport cyclique de 0 (barri�re ferm�e)
    # Calculer le rapport cyclique pour ouvrir la barri�re (� ajuster en fonction de votre servo)
    duty_cycle = (angle_ouverture_barriere / 18.0) + 2.5
    pwm_barriere.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre � la barri�re de s'ouvrir
    pwm_barriere.ChangeDutyCycle(0)  # Arr�ter le signal PWM

# Fonction pour fermer la barri�re
def fermer_barriere():
    pwm_barriere.start(0)  # D�marrer le signal PWM avec un rapport cyclique de 0 (barri�re ouverte)
    # Calculer le rapport cyclique pour fermer la barri�re (� ajuster en fonction de votre servo)
    duty_cycle = (angle_fermeture_barriere / 18.0) + 2.5
    pwm_barriere.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Attendre 1 seconde pour permettre � la barri�re de se fermer
    pwm_barriere.ChangeDutyCycle(0)  # Arr�ter le signal PWM

# D�finir une classe pour g�rer la porte
class ManageDoor(threading.Thread):
    def __init__(self):
        super(ManageDoor, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            # Ins�rez ici la logique de gestion de la porte
            etat_porte = 'Ouverte'  # Par exemple, obtenez cet �tat � partir de vos capteurs
            if etat_porte == 'Ouverte':
                fermer_porte()  # Si la porte est ouverte, fermez-la
            elif etat_porte == 'Fermee':
                ouvrir_porte()  # Si la porte est ferm�e, ouvrez-la
            time.sleep(1)

# D�finir une classe pour g�rer la barri�re
class ManageGate(threading.Thread):
    def __init__(self):
        super(ManageGate, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            # Ins�rez ici la logique de gestion de la barri�re
            etat_barriere = 'Ouverte'  # Par exemple, obtenez cet �tat � partir de vos capteurs
            if etat_barriere == 'Ouverte':
                fermer_barriere()  # Si la barri�re est ouverte, fermez-la
            elif etat_barriere == 'Fermee':
                ouvrir_barriere()  # Si la barri�re est ferm�e, ouvrez-la
            time.sleep(1)

# Arr�ter proprement les moteurs servo lorsque le programme se termine
def cleanup():
    pwm_porte.stop()
    pwm_barriere.stop()
    GPIO.cleanup()

# Configuration des angles d'ouverture et de fermeture pour la porte et la barri�re
angle_ouverture_porte = 90  # � ajuster en fonction de votre servo de porte
angle_fermeture_porte = 0   # � ajuster en fonction de votre servo de porte

angle_ouverture_barriere = 90  # � ajuster en fonction de votre servo de barri�re
angle_fermeture_barriere = 0   # � ajuster en fonction de votre servo de barri�re
