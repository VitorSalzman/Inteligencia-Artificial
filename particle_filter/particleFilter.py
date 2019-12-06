import imutils
import cv2
import math
import time

# Rastreamento da bola de basquete. Codigo origem: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Requisito de download:
# pip install --upgrade imutils
# pip install opencv-python

def centroid(frame,oldcenter):
    blurred = cv2.GaussianBlur(frame, (3, 3), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('c'):
                # cv2.imwrite("pic.png",frame)
                exit()
            return center
        



cap = cv2.VideoCapture('basket.mp4') # poem o nome do arquivo do video do professor aqui

greenLower = (0, 0, 0)
greenUpper = (11, 255, 255)
center = None
oldcenter = None
lap = time.time()
oldlap = lap

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret:
        oldcenter = center
        oldlap = lap
        center = centroid(frame,oldcenter)
        lap = time.time()

        if(center != None) and (oldcenter != None):
            # print(center)
            print("CENTER IS: ",center)
            print("OldCENTER IS: ",oldcenter)
            print("lap: ({}) | oldlap: ({})".format(lap,oldlap))
            dist = math.sqrt(math.pow(center[0]-oldcenter[0],2) + math.pow(center[1]-oldcenter[1],2))
            diftime = lap-oldlap
            print("diftime: ",diftime)
            print("dist",dist)
            velocidade = dist/diftime
            print("velocidade: ",velocidade)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # motivo do loop eterno


    # if cv2.waitKey(1) & 0xFF == ord('c'):
    #     break

cap.release()
cv2.destroyAllWindows()

