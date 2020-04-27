#!/usr/bin/python
# -*- coding: utf-8 -*-
# Servo control
# author: Tony
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

servo_pin = 12
fpwm = 50

''' The a and b variables reflect the relationship
    between the duty cycle and the rotation angle. They
    must match the type of servo you are using.
'''
a = 45
b = 18.0

def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, fpwm)
    pwm.start(2.5)

def setDirection(direction):
    duty = (direction + a)/b
    pwm.ChangeDutyCycle(duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(1) 
   
print "starting"
setup()
for direction in range(0, 181, 90):
    setDirection(direction)    
setDirection(0)    
GPIO.cleanup() 
print "done"
    
