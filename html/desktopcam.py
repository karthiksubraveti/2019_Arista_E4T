import cv2
import sys
def capture(imageName):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return false
    cap.set(3, 320)
    cap.set(4, 240)
    ret, image = cap.read()
    cv2.imwrite(imageName, image)
    cap.release()
    del(cap)
    return ret
if __name__ == "__main__":
    capture("temp.png")
