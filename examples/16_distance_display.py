import time
import socket,signal
import RPi.GPIO as gpio
import math
import Adafruit_CharLCD as LCD
import smbus



def dis():
	trig = 15
	echo = 14
	gpio.setup(trig,gpio.OUT)
	gpio.setup(echo,gpio.IN)

	gpio.output(trig,False)
	time.sleep(0.5)
	
	gpio.output(trig,True)
	time.sleep(0.00001)
	gpio.output(trig,False)

	while gpio.input(echo)==0:
		pulse_start = time.time()

	while gpio.input(echo)==1:
		pulse_end = time.time()

	pulse_duration =  pulse_end - pulse_start

   	distance = pulse_duration * 17150

   	distance = round(distance, 2)

	return distance



# define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 2
# initialize the I2C address for LCD
lcd = LCD.Adafruit_CharLCDBackpack(address = 0x20)
# turn backlight on
lcd.set_backlight(0)
	
try:
    while True:
	lcd.message('{0:0.2f}cm'.format(dis()))
	time.sleep(2)
	lcd.clear()

except KeyboardInterrupt:
	lcd.clear()
        lcd.set_backlight(1)
        gpio.cleanup()

