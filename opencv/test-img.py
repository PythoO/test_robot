import cv2

img = cv2.imread('/home/pi/Pictures/img.jpeg')
cv2.imshow('output', img)
cv2.waitKey(0)