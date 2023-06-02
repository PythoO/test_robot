from pico_i2c_lcd import I2cLcd
from machine import Pin, I2C
 
sda = Pin(0)
scl = Pin(1)
i2c = I2C(0,scl=scl,sda=sda,freq=100000)
for dev in i2c.scan():
    print(dev)
    print(hex(dev))
          
lcd = I2cLcd(i2c, 0x27, 2, 16)
 
while True:
      lcd.move_to(2,0)
      lcd.putstr('Hello world')
      lcd.move_to(0,1)
      lcd.putstr('Hello world 2')