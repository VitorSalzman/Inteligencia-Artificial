import imutils
import cv2
import math
import time
import random
import numpy as np

import particle as p

maxParticles = 500

def start(center):
    vet_particles = []
    for _ in range(maxParticles):
        m = p.particle()
        m.start(center)
        vet_particles.append(m)
    return vet_particles

def prediction(vet_particles):
    # vetAux = [p.particle() for _ in range(maxParticles) ]
    for i,m in enumerate(vet_particles,0):
        m = m.prediction()
    return vet_particles

def correction(vet_particles,center):
    vetAux = [p.particle() for _ in range(maxParticles)]
    for i, m in enumerate(vet_particles, 0):
        m = m.correction(center)

    # return vet_particles

def normalize(vet_particles):
    sumvet = 0
    for m in vet_particles:
        sumvet += m.toNormalize
    
    for i, m in enumerate(vet_particles, 0):
        m = m.normaliza(sumvet)

    # return vet_particles

def resort(vet_particles):
    # print("@@@@@@@VVVVVVV@@@@@@@@@")
    # print_vet_particles(vet_particles)

    sorted_vet_particulas = [p.particle() for _ in range(maxParticles)]
    vetSort = []
    
    size = 0
    for m in vet_particles: # build vetSort, a ultima casa tem q ser 1
        size = size + m.W
        # print("size: {}| peso: {}".format(size,m.W))
        vetSort.append(size)

    # print("check last:",vetSort[-1])
    # print(vetSort)

    n = random.uniform(0,1)
    metodo = False # ir true metodo correto, else metodo q ele deixou

    if metodo:
        print('n vai roda')
        # # verificar aonde esse valor de N se encontra no intervalo de tempo do vetSort
        # # pegar esta posição e usar para buscar a particula na posição no vet_particles
        # # atribuir essa particula "grande" selecionada ao novo vet_particula ate fechar 1 do total de peso analisado
        
        # tot = 0
        # for _ in range(len(vet_particles)):
        #     for i,sz in enumerate(vetSort,0):
        #         if n <= sz:
        #             sorted_vet_particulas.append(vet_particles[i]) # pega a particula 'gorda'
        #             frag = 1 / len(vet_particles)
        #             tot = tot + frag
        #             n = n + frag
        #             # print("frag: {}|tot: {}|n: {}|".format(frag,tot,n))
        #             if n > 1: #se ele extrapolar o 1, n deveria ser adicionado ao N embaixo?
        #                 #perguntar pro professor
        #                 n = 0
        #             break
        
        # print("tot",tot)
    else:
        for z in range(len(vet_particles)):
            for i,sz in enumerate(vetSort,0):
                if n <= sz:
                    # print("casa: {}|sz: {}| n: {}|".format(i, sz, n))
                    M = vet_particles[i]
                    sorted_vet_particulas[z].setAll(M) # pega a particula 'gorda'
                    # print("peso P: ",vet_particles[i].W)
                    n = random.uniform(0,1)
                    break
    # print("@@@@@@@------------@@@@@@@@@")
    # print_vet_particles(sorted_vet_particulas)
    # print("@@@@@@@^^^^^^^^^^^^@@@@@@@@@")

    return sorted_vet_particulas


def drawBox(vet_particles,frame,name):
    # frame = cv2.copyMakeBorder(frame,50,50,50,50,cv2.BORDER_CONSTANT,value= (255,255,255))
    roxo = (153,51,153)
    

    sumX = 0
    sumY = 0

    for m in vet_particles:
        frame = cv2.circle(frame.copy(), (int(m.X), int(m.Y)),2, (242,147,244), -1) #desenha as particulas
        sumX = sumX + m.X
        sumY = sumY + m.Y

    avgX = int(sumX / len(vet_particles))
    avgY = int(sumY / len(vet_particles))

    frame = cv2.circle(frame.copy(),(int(avgX),int(avgY)),100,roxo,2)
    frame = cv2.circle(frame.copy(),(int(avgX),int(avgY)),2,roxo,-1)
    
    text = "avgX: {} | avgY: {}".format(avgX, avgY)
    frame = cv2.putText(frame,text,(avgX+100,avgY+100),cv2.FONT_HERSHEY_SIMPLEX,0.5, roxo,2)
        
    return frame

def calc_avg_particles(vet_particles):
    sumX = 0
    sumY = 0

    for m in vet_particles:
        sumX = sumX + m.X
        sumY = sumY + m.Y

    return (int(sumX / len(vet_particles)),int(sumY / len(vet_particles)))



def print_vet_particles(vet_particles):
    print("v ---------------------- v")
    for m in vet_particles:
        m.print()
    print("^ ---------------------- ^")

def filter_steps(vet_particles,center):
    

        vet_particles_pred = prediction(vet_particles)
        
        if center is not None:
            correction(vet_particles_pred,center)
            normalize(vet_particles)
            vet_particles = resort(vet_particles)
        else:
            vet_particles = vet_particles_pred

        
        return (vet_particles,vet_particles_pred)
