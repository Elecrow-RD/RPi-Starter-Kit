# doorbell

import RPi.GPIO as GPIO
import time

hall_pin = 4
green_pin = 5
red_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(hall_pin, GPIO.IN)

try:
    while True:
        if(GPIO.input(hall_pin) == 0):
            GPIO.output(green_pin, GPIO.HIGH)
            GPIO.output(red_pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(green_pin, GPIO.LOW)
            GPIO.output(red_pin, GPIO.LOW)
            time.sleep(0.5)
        else:
            GPIO.output(green_pin, GPIO.LOW)
            GPIO.output(red_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
