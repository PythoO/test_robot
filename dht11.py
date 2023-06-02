import board
import adafruit_dht
import displayio
import adafruit_displayio_ssd1306
#from RPLCD import i2c
from time import sleep

# constants to initialise the LCD
lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1 
address = 0x27 
port = 1 # 0 on an older Raspberry Pi

i2c = board.I2C()

# Initialise the LCD
#lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
#                  cols=cols, rows=rows)

# Initialize the DHT11
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

#Initialize Oled
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD/306(display_bus, width=WIDTH, height=HEIGHT)

while True:
    splash = displayio.Group()
    display.show(splash)
    
    try:

#        lcd.cursor_mode = 'blink'
#        lcd.close(clear=True)
        temp = dhtDevice.temperature
        hum = dhtDevice.humidity
        print('Temp: {:.1f} C Humidity: {}%'.format(temp, hum))
#        lcd.write_string('Temp: {:.1f} C'.format(temp))
#        lcd.crlf()
#        lcd.write_string('Humd: {}%'.format(hum))
#        lcd.cursor_pos = (3, 19)
        
        
        oled.fill(0)
        oled.show()
        txt = 'Hello'
        oled.draw_text(0,0, text, 2)
    except RuntimeError as error:
        print(error.args[0])
        sleep(2)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    finally:
        sleep(5)