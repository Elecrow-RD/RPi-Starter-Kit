# car tracking

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
ir_pin = 4
green_pin = 5
red_pin = 6

GPIO.setup(ir_pin, GPIO.IN)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)

try:
    while True:
        if(GPIO.input(ir_pin) == 1):
            GPIO.output(green_pin, GPIO.HIGH)
            GPIO.output(red_pin, GPIO.LOW)
            print("on track")

        else:
            GPIO.output(green_pin, GPIO.LOW)
            GPIO.output(red_pin, GPIO.HIGH)
            print("off track")
except KeyboardInterrupt:
    GPIO.cleanup()
