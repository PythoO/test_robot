from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_imu_config(False, True, False)

sense.clear()

r = (255, 0, 0)

while True:
    degree = sense.get_compass()
    print(degree)
    if degree < 45 or degree > 315:
        sense.show_letter('N')
    elif degree < 135:
        sense.show_letter('E')
    elif degree < 225:
        sense.show_letter('S')
    else:
        sense.show_letter('W')
