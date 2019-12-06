import imutils
import cv2

# Rastreamento da bola de basquete. Codigo origem: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Pra cancelar o loop é so segura "c" (uma hora ele para xD)

# Requisito de download:
# pip install --upgrade imutils
# pip install opencv-python

cap = cv2.VideoCapture('basket.mp4') # poem o nome do arquivo do video do professor aqui

greenLower = (0, 0, 0)
greenUpper = (11, 255, 255)

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret:
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
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2) # corpo da bola
                cv2.circle(frame, center, 5, (0, 0, 255), -1) #centro da detecção

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # motivo do loop eterno


    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()
