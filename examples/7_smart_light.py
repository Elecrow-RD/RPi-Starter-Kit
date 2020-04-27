# smart light

import RPi.GPIO as GPIO
import time

pir_pin = 5
led_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(pir_pin, GPIO.IN)

try:
    while True:
        if(GPIO.input(pir_pin) == 1):
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
