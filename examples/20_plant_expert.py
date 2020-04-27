import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import Adafruit_CharLCD as LCD
import spidev
import sys

# set GPIO board mode
GPIO.setmode(GPIO.BCM)
sensor_type = 11
sensor_pin = 5  #temperature&humudity sensor pin

# define LCD column and row size for 16x2 LCD
lcd_columns=16
lcd_rows=2
# initialize the LCD using the pins
lcd=LCD.Adafruit_CharLCDBackpack(address=0x20)
# turn backlight on 
lcd.set_backlight(0)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def readadc(adcnum):
	r = spi.xfer2([1,8+adcnum<<4,0])
	adcout = ((r[1]&3)<<8)+r[2]
	return adcout

try:
    while True:
        moisture_value = readadc(0)
        lcd.message("Mois={}".format(moisture_value))
        time.sleep(2)
        lcd.clear()
        light_value = readadc(1)
        lcd.message("light={}".format(light_value))
        time.sleep(2)
        lcd.clear()
        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
        if humidity is not None and temperature is not None:
            lcd.message("Temp={0:0.1f}\nHumidity={1:0.1f}%".format(temperature, humidity))
            time.sleep(2)
        lcd.clear()

except KeyboardInterrupt:
    lcd.clear()
    lcd.set_backlight(1)
    GPIO.cleanup()
