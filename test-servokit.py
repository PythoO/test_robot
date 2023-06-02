from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

while True:
    print('A')
    kit.servo[0].angle = 180
    kit.servo[1].angle = 180
    kit.servo[7].angle = 180
    time.sleep(1)

    kit.servo[0].angle = 90
    kit.servo[1].angle = 90

    time.sleep(2)

    print('B')
    kit.servo[0].angle = 0
    kit.servo[1].angle = 0
    kit.servo[7].angle = 0
    time.sleep(1)
