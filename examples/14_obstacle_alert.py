#!/usr/bin/python
# -*- coding: utf-8 -*-
# Obstacle alert
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
buzzer_pin = 6
GPIO.setup(buzzer_pin, GPIO.OUT)

def dis():
  TRIG = 15
  ECHO = 14


  GPIO.setup(TRIG,GPIO.OUT)
  GPIO.setup(ECHO,GPIO.IN)

  GPIO.output(TRIG, False)
  time.sleep(0.5)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  print("Distance: %s cm" % distance)
  return distance

try:
  while True:
    distance = dis()
    if distance < 20:
      GPIO.output(buzzer_pin, GPIO.HIGH)
    else:
      GPIO.output(buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
  GPIO.cleanup()
