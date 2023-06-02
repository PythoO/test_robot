from sense_hat import *
from time import sleep

sense = SenseHat()

r = (255, 0, 0)
o = (255, 128, 0)
y = (255, 255, 0)
g = (0, 255, 0)
c = (0, 255, 255)
b = (0, 0, 255)
p = (255, 0, 255)
n = (255, 128, 128) # pink
w = (255, 255, 255)
k = (0,0,0) # blank

while True:
    sense.clear()
    sense.set_pixel(0, 0, r)
    sleep(60)
    sense.clear()
    pressure = sense.pressure
    temp = sense.temp
    hum = sense.humidity
    data = [temp, hum, pressure]
    myfile = open('weather.txt', 'a')
    myfile.write(str(data))
    myfile.write('\n')
    myfile.close()