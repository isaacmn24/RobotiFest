from gpiozero import Servo

servo = Servo(15)

def cerrar_garra():
    servo.min()

def abrir_garra():
    servo.mid()
