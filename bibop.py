# BI-BOP
from gpiozero import Robot, Servo
from time import sleep
from pynput.keyboard import Listener
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
bibop = Robot(left=(7,8), right=(9,10))
head_servo = Servo(14, pin_factory=factory)

robot_run = True

def on_press(key):
    try:
        #print('IN : {}'.format(key.char))
        if key.char == '1':
            head_servo.min()
        elif key.char =='3':
            head_servo.max()
        elif key.char == '2':
            head_servo.mid()
        elif key.char == 'w':
            bibop.forward(speed=0.5, curve_left=0.0)
        elif key.char == 's':
            bibop.stop()
        elif key.char == 'x':
            bibop.backward(speed=0.5, curve_left=0.1)
        elif key.char == 'a':
            bibop.right(speed=0.3)
        elif key.char == 'd':
            bibop.left(speed=0.3)
    except AttributeError:
        print('Special key {0} pressed'.format(key))


with Listener(on_press=on_press) as listener:
    listener.join()

