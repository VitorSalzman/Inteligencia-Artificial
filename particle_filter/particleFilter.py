import imutils
import cv2
import math
import time
import random
import numpy as np

# Rastreamento da bola de basquete. Codigo origem: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Requisito de download:
# pip install --upgrade imutils
# pip install opencv-python

class particle():

    def __init__(self,center):
        # self.X = random.gauss(center[0],50)
        # self.Y = random.gauss(center[1],50)
        self.X = center[0]
        self.Y = center[1]
        self.Vx = random.uniform(0, vel)  # velocidade 1549 pixels/sec
        self.Vy = random.uniform(0, vel)  # velocidade 1549 pixels/sec
        self.W = 0
        self.toNormalize = 0

    def prediction(self):
        self.X = self.X + (deltaT * self.Vx)
        self.Y = self.Y + (deltaT * self.Vy)
        self.Vx = self.Vx + random.gauss(0, pow(vel * 0.1, 2))
        self.Vy = self.Vy + random.gauss(0, pow(vel * 0.1, 2))

    def correction(self,center):
        Dt = math.sqrt(pow((center[0] - self.X), 2) + pow((center[1] - self.Y), 2))
        self.toNormalize = 1/(np.exp(Dt))

    # def normaliza(self,sumToNormalize):
    #     self.W = self.toNormalize/sumToNormalize

def start(center):
    vet_particles = [particle(center) for _ in range(maxParticles)] #verificar se esta criando particulas corretamente
    return vet_particles

def prediction(vet_particles):
    for m in vet_particles:
        m.prediction()
    return vet_particles

def correction(vet_particles,center):
    for m in vet_particles:
        m.correction(center)
    return vet_particles

def normalize(vet_particles):
    vetToNormalize = []
    for m in vet_particles:
        vetToNormalize.append(m.toNormalize)

    sumToNormalize = sum(vetToNormalize)
    # print('stn:',sumToNormalize)

    for m in vet_particles:
        m.W = m.toNormalize/sumToNormalize
        # m.normaliza(sumToNormalize)

    return vet_particles

def resort(vet_particles):
    # print("@@@@@@@VVVVVVV@@@@@@@@@")
    # print_vet_particles(vet_particles)
    sorted_vet_particulas = []
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
        #
        # tot = 0
        # for _ in range(len(vet_particles)):
        #     for i,sz in enumerate(vetSort,0):
        #         if n <= sz:
        #             sorted_vet_particulas.append(vet_particles[i]) # pega a particula 'gorda'
        #             frag = 1 / len(vet_particles)
        #             tot = tot + frag
        #             n = n + frag
        #             print("frag: {}|tot: {}|n: {}|".format(frag,tot,n))
        #             if n > 1: #se ele extrapolar o 1, n deveria ser adicionado ao N embaixo?
        #                 #perguntar pro professor
        #                 n = 0
        #             break
        #
        # print("tot",tot)
    else:
        for _ in range(len(vet_particles)):
            for i,sz in enumerate(vetSort,0):
                if n <= sz:
                    # print("casa: {}|sz: {}| n: {}|".format(i, sz, n))
                    sorted_vet_particulas.append(vet_particles[i]) # pega a particula 'gorda'
                    # print("peso P: ",vet_particles[i].W)
                    n = random.uniform(0,1)
                    break
    # print("@@@@@@@------------@@@@@@@@@")
    # print_vet_particles(sorted_vet_particulas)
    # print("@@@@@@@^^^^^^^^^^^^@@@@@@@@@")

    return sorted_vet_particulas

def drawParticles(vet_particles,frame):
    for m in vet_particles:
        frame = cv2.circle(frame.copy(), (int(m.X), int(m.Y)), 3, (255, 0, 255), 2)  # desenha as particulas

    cv2.imshow("particles",frame)

def drawBox(vet_particles,frame):
    sumX = 0
    sumY = 0

    for m in vet_particles:
        frame = cv2.circle(frame.copy(), (int(m.X), int(m.Y)),2, (255, 0, 0), -1) #desenha as particulas
        sumX = sumX + m.X
        sumY = sumY + m.Y

    avgX = sumX / len(vet_particles)
    avgY = sumY / len(vet_particles)

    frame = cv2.circle(frame.copy(),(int(avgX),int(avgY)),100,(0,255,0),2)
    cv2.imshow("predicted",frame)


def centroid(frame):
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
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('c'):
                # cv2.imwrite("pic.png",frame)
                return False
            return center

def print_vet_particles(vet_particles):
    print("v ---------------------- v")
    for m in vet_particles:
        print("X: {}|Y: {}| Vx: {}| Vy: {}| W: {}| tN: {}|".format(m.X,m.Y,m.Vx,m.Vy,m.W,m.toNormalize))
    print("^ ---------------------- ^")


# calculaVelocidadeMedia não e utilizado
def calculaVelocidadeMedia():
    center = None
    lap = time.time()
    lst = []

    while (cap.isOpened()):

        ret, frame = cap.read()
        if ret:
            oldcenter = center
            oldlap = lap
            center = centroid(frame)
            lap = time.time()

            if (center != None and center != False) and (oldcenter != None):
                # print(center)
                print("CENTER IS: ", center)
                print("OldCENTER IS: ", oldcenter)
                print("lap: ({}) | oldlap: ({})".format(lap, oldlap))
                dist = math.sqrt(math.pow(center[0] - oldcenter[0], 2) + math.pow(center[1] - oldcenter[1], 2))
                diftime = lap - oldlap
                print("diftime: ", diftime)
                print("dist", dist)
                velocidade = dist / diftime
                print("velocidade: ", velocidade)
                lst.append(velocidade)

    mediaVel = sum(lst) / len(lst)
    print("mediaVel: ", mediaVel)
    return mediaVel

cap = cv2.VideoCapture('basket.mp4') # poem o nome do arquivo do video do professor aqui

greenLower = (0, 0, 0)
greenUpper = (11, 255, 255)

global deltaT, vel, maxParticles
deltaT = 1/10
vel = 150
maxParticles = 100

flag = 0

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret:
        center = centroid(frame)
        if center == None: continue

        print("center",center)

        if flag ==0:
            print("start")
            vet_particles = start(center)
            # drawParticles(vet_particles,frame)
            flag = 1

        print("prediction")
        vet_particles = prediction(vet_particles)
        # drawParticles(vet_particles, frame)
        # cv2.waitKey(0)
        # print_vet_particles(vet_particles)

        print("correction")
        vet_particles = correction(vet_particles,center)
        # drawParticles(vet_particles, frame)
        # cv2.waitKey(0)
        # print_vet_particles(vet_particles)

        print("normalize")
        vet_particles = normalize(vet_particles)
        # drawParticles(vet_particles, frame)
        # cv2.waitKey(0)
        # print_vet_particles(vet_particles)

        print("resort")
        vet_particles = resort(vet_particles)
        # drawParticles(vet_particles, frame)
        # cv2.waitKey(0)
        # print_vet_particles(vet_particles)

        drawBox(vet_particles,frame)


        if(center == False):
            break

    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # motivo do loop eterno


    if cv2.waitKey(0) & 0xFF == ord('c'):
        break


cap.release()
cv2.destroyAllWindows()

