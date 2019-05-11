from picamera import PiCamera
import time

def capture(filename):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.capture(filename)
    return True
