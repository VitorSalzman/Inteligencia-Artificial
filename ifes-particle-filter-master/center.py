import argparse
import cv2
import time

import particle_filter as pf
import pf_tools as pft
import pre_process as pp

#Construindo a estrutura de argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

#Lendo o video com OpenCV
video  = cv2.VideoCapture(args["video"])

#Inicializando o filtro de particulas
lst_particulas = pft.initialize_pf((1277,399))

while True:
    #Captura o frame atual
    cap, frame = video.read()

    #Verifica se esta no final do Video
    if frame is None:
        break

    contour = pp.getFrameContour(frame)

    #Verificando se pelo menos um contorno foi identificado
    if len(contour) > 0:

        radius, center = pp.getCenterOfContour(contour)

        #Aplicando o filtro de particulas com relacao ao centro
        lst_particulas = pf.filtro_de_particulas(center,lst_particulas)

        #Printando cada particula
        for part in lst_particulas:
            cv2.circle(frame, (int(part.pos_x),int(part.pos_y)), 5, (0, 255, 255), 2)

        if radius > 10:
            #Printando o circulo calculado pela média das partículas
            cv2.circle(frame, pft.media_pos(lst_particulas), int(radius),(0, 255, 255), 2)
            #Printando a centroid obtida pelo OpenCV
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

        #Exibindo o frame de saída
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        #Se apertar a tecla "q", interrompe o Loop
        if key == ord("q"):
            break

#fechar video e janelas
video.release()
cv2.destroyAllWindows()
