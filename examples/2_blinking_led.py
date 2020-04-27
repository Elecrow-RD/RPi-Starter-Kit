# Blinking light

import RPi.GPIO as GPIO
import time

led_pin  = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

GPIO.output(led_pin, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(led_pin, GPIO.LOW)
GPIO.cleanup()
