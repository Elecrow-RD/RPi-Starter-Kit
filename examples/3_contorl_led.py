# control LED

import RPi.GPIO as GPIO

led_pin = 5
button_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

try:
    while True:
        if(GPIO.input(button_pin) == 1):
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
