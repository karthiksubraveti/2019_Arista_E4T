import time
'''
   Enable if you have connected raspberry pie camera module

'''
'''
from picamera import PiCamera
def capture(filename):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture(filename)
    camera.stop_preview()
    camera.close()
    return True
'''
'''
    Disable the following code if you have raspberry pi camera module
    attached
'''
import cv2
def capture(filename):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
       return false
    cap.set(3, 320)
    cap.set(4, 240)
    ret, image = cap.read()
    cv2.imwrite(filename, image)
    cap.release()
    del(cap)
    return ret
