from gpiozero import Servo
from time import sleep
from pynput.keyboard import Listener

myGpio = 14
servo = Servo(myGpio)

def on_press(key):
    try:
        print('IN : {}'.format(key.char))
        if key.char == '1':
            servo.min()
        elif key.char =='3':
            servo.max()        
        elif key.char == '2':
            servo.mid()
    except AttributeError:
        print('Special key {0} pressed'.format(key))
        
with Listener(on_press=on_press) as listener:
    listener.join()
