#!/usr/bin/env python

"""
SNAPS Is simple Toolfor Taking Snapshots From A WebCam.
The Images Are Saved In Current Directory Named According
To The Time They Were Taken. Including Date and Year....

Usage:
    Press 's' To TAKE SnapShot.
    Press 'q' To QUIT.
"""

import cv2
import time


def snapshot():
    cap = cv2.VideoCapture(-1)

    counter = 0  # Initialize frame counter

    while(True):
        ret, video = cap.read()
        counter += 1  # Increment frame counter
        if counter == 30:  # Check if 30 frames have passed
            now = time.asctime()
            break

    cap.release()
    return video
