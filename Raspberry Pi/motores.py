import RPi.GPIO as GPIO
import time

Motores = [
    [2, 3],
    [10, 9],
    [17, 27],
    [23, 24]
    ]

GPIO.setmode(GPIO.BCM)

for motor in Motores:
    for pin in motor:
        GPIO.setup(pin, GPIO.OUT)

def main():

    print("Hola")

    for motor in range(4):
        Avance(motor)
    time.sleep(10)

    for motor in range(4):
        Retroceso(motor)
    time.sleep(10)

    Giro180()

    return


def Avance(Motor):
    GPIO.output(Motores[Motor][0], GPIO.HIGH)
    GPIO.output(Motores[Motor][1], GPIO.LOW)
    return

def Retroceso(Motor):
    GPIO.output(Motores[Motor][0], GPIO.LOW)
    GPIO.output(Motores[Motor][1], GPIO.HIGH)
    return

def Paro(Motor):
    GPIO.output(Motores[Motor][0], GPIO.LOW)
    GPIO.output(Motores[Motor][1], GPIO.LOW)
    return

def Giro180():
    Avance(0)
    Avance(1)
    Retroceso(2)
    Retroceso(3)

    time.sleep(5)

    Paro(0)
    Paro(1)
    Paro(2)
    Paro(3)

    return

#main()