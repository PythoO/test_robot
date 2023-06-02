from gpiozero import Servo, Robot
import cv2
import numpy as np
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
from time import sleep


rob = Robot(left=(7,8), right=(9,10))

factory = PiGPIOFactory()
head_servo = Servo(14, pin_factory=factory)

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 320)

_, frame = cap.read()
rows, cols, _ = frame.shape
x_medium = int(cols / 2)
center = int(cols / 2)
position = 0

y = 0
x = 0
w = 0
h = 0

while True:
    _, frame = cap.read()
    flipVertical = cv2.flip(frame, 0)
    hsv_frame = cv2.cvtColor(flipVertical, cv2.COLOR_BGR2HSV)
    
    # red color
    low_red = np.array([150, 155, 100])
    high_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        x_medium = int((x + x + w) / 2)     
        break
    
    #cv2.line(flipVertical, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    #cv2.rectangle(flipVertical,(x,y),(x+w,y+h),(0,255,0),2)
    
    # Move servo motor
    if x_medium < center -20:
        position += 0.02
        rob.stop()
    elif x_medium > center + 20:
        position -= 0.02
        rob.stop() 
    else:
        rob.stop()
        
    if position > 0.5:
        rob.left(speed=0.1)
    elif position < -0.5:
        rob.right(speed=0.1)
    elif w < 50:
        rob.forward(speed=0.1)
    elif w > 70:
        rob.backward(speed=0.1)
    else:
       rob.stop()
        
    position = round(position,2)
    print(position, w)
    
    if position > 1:
        position = 1
    elif position < -1:
        position = -1
        
    head_servo.value = position
    
    
    #cv2.line(flipVertical, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    cv2.rectangle(flipVertical,(x_medium,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Frame", flipVertical)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()