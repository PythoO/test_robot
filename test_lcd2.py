from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0, sda=Pin(0), scl=Pin(1), frq=400000)
