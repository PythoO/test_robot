from gpiozero import Robot, DistanceSensor
from time import sleep

robby = Robot(left=(7,8), right=(9,10))
distance_sensor = DistanceSensor(trigger=18, echo=24)

while True:
    sleep(1)
    # distance en CM
    distance = distance_sensor.distance * 100
    if (distance > 20):
        robby.forward()
    if (distance < 10):
        robby.forward(0.25)
    if (distance <  5):
        robby.stop()
    
    print(distance)


