from sense_hat import SenseHat
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

rainbow = [r, o, y, g, c, b, p, n]

heart = [
    k,r,r,k,k,r,r,k,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    k,r,r,r,r,r,r,k,
    k,k,r,r,r,r,k,k,
    k,k,k,r,r,k,k,k
]

pumpkin = [
    k,k,k,o,o,k,k,k,
    k,o,o,o,o,o,o,k,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    k,o,o,o,o,o,o,k,
    k,k,k,o,o,k,k,k,
]

while True:
    sense.clear()
    sense.set_pixels(heart)
    sleep(5)
  
    for y in range(8):
        colour = rainbow[y]
        for x in range(8):
            sense.set_pixel(x, y, colour)
            
        sleep(1)
    sleep(3)
    
    sense.clear()
    sense.set_pixels(pumpkin)
    sleep(5)

