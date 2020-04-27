import spidev
import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
motor_pin = 12
GPIO.setup(motor_pin, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

pwm = GPIO.PWM(motor_pin,80)
pwm.start(0)

def readadc(adcnum):
	r = spi.xfer2([1,8+adcnum<<4,0])
	adcout = ((r[1]&3)<<8)+r[2]
	return adcout

def brightness_func(x):
        return x/10.23

try:
        while True:
            value = readadc(0)
            brightness = brightness_func(value)
            pwm.ChangeDutyCycle(brightness)
            time.sleep(0.1)

except KeyboardInterrupt:
        GPIO.cleanup()
