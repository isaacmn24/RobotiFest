import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while ():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
