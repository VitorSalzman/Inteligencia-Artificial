import cv2
import numpy as np

cap = cv2.VideoCapture("bouncingBall.mp4")

while(cap.isOpened()):
    ret, frame = cap.read() 
    #cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    if ret:
        cv2.imshow("Image", frame)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", hsv)
        # define range of blue color in HSV
        lower_blue = np.array([50,50,90])
        upper_blue = np.array([255,255,190])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
    else:
       print('end video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(5) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()


'''
Buscar imagem (video)
Reconhecer o objeto (usar HSV, ou otsu)
Centro de Massa


x = [(Xi,Yi,Vx,Vy,P),....]


P = [

    Xt = Xt-1 + ▲TxVxt-1
    Yt = Y-1 + ▲TxVxt-1
    Vxt = Vxt-1 + N(u,o²)
    Vyt = Vyt-1 + N(u,o²)

]

correção [
    dmt = sqrt( (Cxt = Xmt)² + (Cyt - Ymt)² )
    Wmt = 1/e^(dmt)
]

normalizar (W) [
    Wmt = Wmt/ ΣW
]

Resorteio [
    Gerar x aleatorio entre [0,1]
    S = W/N; w=1 (que?)
    Sortei os [1,m]
    1º n
    n+S
]

Media Ponderada W=Ê
Box = Ê = (X^,Y^)

'''