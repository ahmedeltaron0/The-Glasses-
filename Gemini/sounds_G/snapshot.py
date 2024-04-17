
import cv2
import time


def snapshot():
    cap = cv2.VideoCapture(0)

    counter = 0  # Initialize frame counter

    while(True):
        ret, video = cap.read()
        counter += 1  # Increment frame counter
        if counter == 30:  # Check if 30 frames have passed
            now = time.asctime()
            break

    cap.release()
    return video
