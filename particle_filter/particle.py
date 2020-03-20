import imutils
import cv2
import math
import time
import random
import numpy as np

deltaT = 1/30
VELMAX = 3000

class particle():

    def __init__(self):
        self.X = None
        self.Y = None
        self.Vx = None
        self.Vy = None
        self.W = 0
        self.toNormalize = 0

    def setAll(self,particle):
        self.X = int(particle.X)
        self.Y = int(particle.Y)
        self.Vx = particle.Vx
        self.Vy = particle.Vy
        self.W = particle.W
        self.toNormalize = particle.toNormalize

    def start(self,center):
        # self.X = random.gauss(center[0],50)
        # self.Y = random.gauss(center[1],50)
        self.X = int(center[0])
        self.Y = int(center[1])
        self.Vx = random.uniform(-VELMAX, VELMAX)  # velocidade 1549 pixels/sec
        self.Vy = random.uniform(-VELMAX, VELMAX)  # velocidade 1549 pixels/sec
        self.W = 0
        self.toNormalize = 0

    def prediction(self):
        # REVER ESSA FUNÇÃO DE VELOCIDADE QUE TA MUITO ESTRANHA, ELA ESTA BATENDO O LIMITE TODA HORA

        # print(" ------------- PRED INI ------------- ")

        a = pow(VELMAX * 0.01, 2)
        b = random.gauss(0, a)
        self.Vx = self.Vx + b
        # print("pow(VELMAX * 0.1, 2): {: >10.3f}| random.gauss(0, a): {: >10.3f}| Vx: {: >10.3f}|".format(a, b, self.Vx))

        b = random.gauss(0, a)
        self.Vy = self.Vy + b
        # print("pow(VELMAX * 0.1, 2): {: >10.3f}| random.gauss(0, a): {: >10.3f}| Vy: {: >10.3f}|".format(a, b, self.Vy))

        if self.Vx > VELMAX :
            self.Vx = VELMAX

        if self.Vy > VELMAX :
            self.Vy = VELMAX

        if self.Vx < -VELMAX :
            self.Vx = -VELMAX

        if self.Vy < -VELMAX :
            self.Vy = -VELMAX

        a = deltaT * self.Vx
        self.X = int(self.X + a)
        # print("deltaT * self.Vx: {}|self.X + a: {}".format(a, self.X))

        a = deltaT * self.Vy
        self.Y = int(self.Y + a)
        # print("deltaT * self.Vy: {}|self.Y + a: {}".format(a, self.Y))
        # print(" ------------- PRED END ------------- ")

        return self

    def correction(self,center):
        Dt = math.sqrt(pow((center[0] - self.X), 2) + pow((center[1] - self.Y), 2))
        # self.toNormalize = 1/(np.exp( Dt ))
        self.toNormalize = np.exp( -Dt )
        return self

    def normaliza(self,sumToNormalize):
        self.W = self.toNormalize/sumToNormalize
        return self

    def print(self):
        print("X: {: >5}|Y: {: >5}| Vx: {: >10.3f}| Vy: {: >10.3f}| W: {: >8.3f}| tN: {: >5.15f}|".format(self.X, self.Y, self.Vx, self.Vy, self.W, self.toNormalize))
        return self