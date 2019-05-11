from picamera import PiCamera
import time

def capture(filename):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture(filename)
    camera.stop_preview()
    camera.close()
    return True
