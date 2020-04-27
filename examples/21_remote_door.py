#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time
import socket, signal
import lirc

# define relay pin
servo_pin = 12

a = 45
b = 18.0
fpwm = 50


def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, fpwm)
    pwm.start(2.5)

def setDirection(direction):
    duty = (direction +a)/b
    pwm.ChangeDutyCycle(duty)
    print "direction =", direction, "-> duty =", duty
   


# setup the IR pins
PORT = 42001
HOST = "localhost"
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Lirc = lirc.init("keys")

def handler(signal, frame):
	Socket.close()
	GPIO.cleanup()
	exit(0)

signal.signal(signal.SIGTSTP, handler)

def sendCmd(cmd):
    n = len(cmd)
    a = array('c')
    a.append(chr((n >> 24) & 0xFF))
    a.append(chr((n >> 16) & 0xFF))
    a.append(chr((n >> 8) & 0xFF))
    a.append(chr(n & 0xFF))
    Socket.send(a.tostring() + cmd)
try:
    setup()
    print("starting")
    while True:
        output = lirc.nextcode()[0]
        print(output)
        if(output == "VOL_UP"):
            # rotate to 180
            setDirection(180)
        elif(output == "VOL_DWN"):
            # rotate to 0
            setDirection(0)
except KeyboardInterrupt:
    GPIO.cleanup()
