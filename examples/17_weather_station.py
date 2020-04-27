# Weather station

import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import Adafruit_CharLCD as LCD

# set GPIO board mode
GPIO.setmode(GPIO.BCM)

sensor_type = 11
sensor_pin = 5  #temperature&humudity sensor pin
led_pin = 6

GPIO.setup(led_pin, GPIO.OUT)
# define LCD column and row size for 16x2 LCD
lcd_columns=16
lcd_rows=2
# initialize the LCD using the pins
lcd=LCD.Adafruit_CharLCDBackpack(address=0x20)
# turn backlight on 
lcd.set_backlight(0)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
        if humidity is not None and temperature is not None:
            lcd.message("Temp={0:0.1f}\nHumidity={1:0.1f}%".format(temperature, humidity))
            
            if temperature < 10 or temperature > 35:
                GPIO.output(led_pin, GPIO.HIGH)
            else:
                    GPIO.output(led_pin, GPIO.LOW)
            time.sleep(1)
        lcd.clear()
except KeyboardInterrupt:
    lcd.clear()
    lcd.set_backlight(1)
    GPIO.cleanup()
                
