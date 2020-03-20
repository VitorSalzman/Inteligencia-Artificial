import cv2

import pf_tools as pf
import image_process as ip

# Rastreamento da bola de basquete. Codigo origem: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Requisito de download:
# pip install --upgrade imutils
# pip install opencv-python


cap = cv2.VideoCapture('basket.mp4') # poem o nome do arquivo do video do professor aqui

flag = 0

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret:
        center = ip.find_centroid(frame)
        if center == None: continue

        # print("center",center)

        if flag ==0:
            # print("start")
            vet_particles = pf.start(center)
            # drawParticles(vet_particles,frame)
            flag = 1
        
        vet_particles = pf.filter_steps(vet_particles,center,frame) #remover esse frame quando estiver funcionando

        
        # pf.print_vet_particles(vet_particles.copy())
        # pf.drawBox(vet_particles.copy(),frame)


        if(center == False):
            break


    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # motivo do loop eterno


    if cv2.waitKey(1) & 0xFF == ord('c'):
        break


cap.release()
cv2.destroyAllWindows()

