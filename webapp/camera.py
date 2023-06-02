#camera.py
# import the necessary packages
import cv2
# defining face detector
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.9

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()
        
    def get_frame(self):
       #extracting frames
        sucess, image = self.video.read()
        image = cv2.flip(image, 0)
        resized_img=cv2.resize(image,(320,240), interpolation=cv2.INTER_AREA)                    
        gray=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
         cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,255,0),2)
         break
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', resized_img)
        return jpeg.tobytes()