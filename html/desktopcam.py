from picamera import PiCamera
import time

def capture(filename):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # sleep for the camera to warmup
    time.sleep(1)
    camera.capture(filename)
    return True
