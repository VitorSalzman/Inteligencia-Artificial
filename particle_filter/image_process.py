
import imutils
import cv2
import math
import time
import random
import numpy as np

greenLower = (0, 0, 0)
greenUpper = (11, 255, 255)

def find_centroid(frame):    
    blurred = cv2.GaussianBlur(frame, (3, 3), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 3, (0, 255, 255), -1)
            text = "avgX: {} | avgY: {}".format(int(x), int(y))
            frame = cv2.putText(frame,text,(int(x)+100,int(y)+100),cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255),2)
            
            # cv2.imshow("Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('c'):
                # cv2.imwrite("pic.png",frame)
                return False
            return center