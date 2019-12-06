import imutils
import cv2
import math
import time
import random

# Rastreamento da bola de basquete. Codigo origem: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Requisito de download:
# pip install --upgrade imutils
# pip install opencv-python

class particle():

    def __init__(self,center):
        self.X = center[0]
        self.Y = center[1]
        self.Vx = random.uniform(0, vel)  # velocidade 1549 pixels/sec
        self.Vy = random.uniform(0, vel)  # velocidade 1549 pixels/sec
        self.W = 0
        self.toNormalize = None

    def prediction(self):
        self.X = self.X + deltaT * vel
        self.Y = self.Y + deltaT * vel
        self.Vx = self.Vx + random.gauss(0, pow(vel * 0.1, 2))
        self.Vy = self.Vy + random.gauss(0, pow(vel * 0.1, 2))

    def correction(self,center):
        Dt = math.sqrt(pow(center[0] - self.X, 2) + pow(center[1] - self.Y, 2))
        self.toNormalize = 1/math.exp(Dt)

    def normalize(self,sumToNormalize):
        self.W = self.W/sumToNormalize

def start(center):
    vet_particulas = [particle(center) for _ in range(maxParticles)] #verificar se esta criando particulas corretamente
    return vet_particulas

def prediction(vet_particulas):
    for m in vet_particulas:
        m.prediction()

def correction(vet_particulas,center):
    for m in vet_particulas:
        m.correction(center)

def normalize(vet_particulas):
    vetToNormalize = []
    for m in vet_particulas:
        vetToNormalize.append(m.toNormalize)

    sumToNormalize = sum(vetToNormalize)

    for m in vet_particulas:
        m.normalize(sumToNormalize)

def resort(vet_particulas):
    sorted_vet_particulas = []
    vetSort = []
    size = 0
    # for count,m in enumerate(vet_particulas,0):
    for m in vet_particulas: # build vetSort, a ultima casa tem q ser 1
        size = size + m.W
        vetSort.append(size)

    print("check last:",vetSort[-1]) #funfa?

    size = 0
    n = random.uniform(0,1)

    # verificar aonde esse valor de N se encontra no intervalo de tempo do vetSort
    # pegar esta posição e usar para buscar a particula na posição no vet_particulas
    # atribuir essa particula "grande" selecionada ao novo vet_particula ate fechar 1 do total de peso analisado
    while size <= 1:
        for i,sz in enumerate(vetSort,0):
            if sz >= n:
                sorted_vet_particulas.append(vet_particulas.__getitem__(i)) # pega a particula 'gorda'
                size = size + n
                n = n + 1 / len(vet_particulas)
                break

    return sorted_vet_particulas


def drawBox(vet_particles,frame):
    sumX,sumY = 0

    for m in vet_particulas:
        sumX = sumX + m.X
        sumY = sumY + m.Y

    avgX = sumX / len(vet_particles)
    avgY = sumY / len(vet_particles)

    frame = cv2.circle(frame,(avgX,avgY),100,(0,255,0),2)
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

cap = cv2.VideoCapture('basket.mp4') # poem o nome do arquivo do video do professor aqui

greenLower = (0, 0, 0)
greenUpper = (11, 255, 255)

global deltaT, vel, maxParticles
deltaT = 1/30
vel = 1549
maxParticles = 500


while(cap.isOpened()):

    ret, frame = cap.read()
    if ret:
        center = centroid(frame)

        vet_particles = start(center)
        vet_particles = prediction(vet_particles)
        vet_particles = correction(vet_particles,center)
        vet_particles = normalize(vet_particles)
        vet_particles = resort(vet_particles)
        drawBox(vet_particles,frame)


        if(center == False):
            break

    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) # motivo do loop eterno


    # if cv2.waitKey(1) & 0xFF == ord('c'):
    #     break

mediaVel = sum(lst) / len(lst)
print("mediaVel: ",mediaVel)
cap.release()
cv2.destroyAllWindows()

