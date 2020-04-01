import imutils
import cv2
import math
import time
import random
import numpy as np

import particle as p

# maxParticles = 500


class ParticleFilter():

    def __init__(self,maxParticles,center,maxFrameLost):
        self.maxParticles = maxParticles
        self.__vet_particles = self.__start(center)
        self.vet_particles_predicted = None
        self.maxFrameLost = maxFrameLost
        self.__countToMaxFrameLost = 0

    def __start(self,center):
        vet_particles = []
        for _ in range(self.maxParticles):
            particle = p.particle()
            particle.start(center)
            vet_particles.append(particle)

        return vet_particles

    def __prediction(self):
        for particle in self.__vet_particles:
            particle = particle.prediction()
        
        return self.__vet_particles

    def __correction(self,center):
        for particle in self.__vet_particles:
            particle = particle.correction(center)

    def __normalize(self):
        sumvet = 0
        for particle in self.__vet_particles:
            sumvet += particle.toNormalize
        
        for particle in self.__vet_particles:
            particle = particle.normaliza(sumvet)


    def __resort(self):
        sorted_vet_particulas = [p.particle() for _ in range(self.maxParticles)]
        vetSort = []
        
        sumWeight = 0
        for particle in self.__vet_particles:
            sumWeight = sumWeight + particle.weight
            vetSort.append(sumWeight)

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
            for z in range(len(self.__vet_particles)): #for z in range(self.maxParticles): <<< testa isso dps
                for i,sz in enumerate(vetSort,0):
                    if n <= sz:
                        # print("casa: {}|sz: {}| n: {}|".format(i, sz, n))
                        particle = self.__vet_particles[i]
                        sorted_vet_particulas[z].setAll(particle) # pega a particula 'gorda'
                        # print("peso P: ",vet_particles[i].W)
                        n = random.uniform(0,1)
                        break
        
        self.__vet_particles = sorted_vet_particulas
        return sorted_vet_particulas


    def drawBox(self,frame):
        # frame = cv2.copyMakeBorder(frame,50,50,50,50,cv2.BORDER_CONSTANT,value= (255,255,255))
        roxo = (153,51,153)
        

        sumX = 0
        sumY = 0

        for particle in self.vet_particles_predicted:
            frame = cv2.circle(frame.copy(), (int(particle.X), int(particle.Y)),2, (242,147,244), -1) #desenha as particulas
            sumX = sumX + particle.X
            sumY = sumY + particle.Y

        avgX = int(sumX / self.maxParticles)
        avgY = int(sumY / self.maxParticles)

        cv2.circle(frame,(int(avgX),int(avgY)),100,roxo,2)
        cv2.circle(frame,(int(avgX),int(avgY)),2,roxo,-1)
        
        text = "avgX: {} | avgY: {}".format(avgX, avgY)
        cv2.putText(frame,text,(avgX+100,avgY+100),cv2.FONT_HERSHEY_SIMPLEX,0.5, roxo,2)
            
        return frame

    def __print_vet_particles(self,vet):
        print("v ---------------------- v")
        for particle in vet:
            particle.print()
        print("^ ---------------------- ^")

    def filter_steps(self,center):
        self.vet_particles_predicted = self.__prediction()

        if center is not None:
            print("| tracking |")
            self.__correction(center)
            self.__normalize()
            self.__resort()
            self.__countToMaxFrameLost = 0
        else:
            print("|> missing center <| cont: {} | max: {} to lose tracking.".format(self.__countToMaxFrameLost,self.maxFrameLost))
            self.__vet_particles = self.vet_particles_predicted
            self.__countToMaxFrameLost = self.__countToMaxFrameLost + 1

        if self.__countToMaxFrameLost >= self.maxFrameLost:
            self.__vet_particles = None
            print("|X LOST TRACKING X|")
            return False

        return self.vet_particles_predicted
