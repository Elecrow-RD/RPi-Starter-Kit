# doorbell

import RPi.GPIO as GPIO
import time

touch_pin = 5
buzzer_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(touch_pin, GPIO.IN)

try:
    while True:
        if(GPIO.input(touch_pin) == 1):
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(3)
        else:
            GPIO.output(buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
