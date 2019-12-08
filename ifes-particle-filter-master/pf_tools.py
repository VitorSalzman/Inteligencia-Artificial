from particle import particula
import numpy as np
import random
import math

V_MIN = -500.0
V_MAX = 500.0
NUM_PARTICULAS = 100
STD_DEV_V = 200.0
STD_DEV_T = 0.5
DELTA_TIME = 0.05

def media_pos(lst_particulas):
    sum_x = 0
    sum_y = 0
    for part in lst_particulas:
        sum_x = sum_x + part.pos_x
        sum_y = sum_y + part.pos_y
    return(int(sum_x/NUM_PARTICULAS),int(sum_y/NUM_PARTICULAS))
def normalize_theta(theta):
    return None

def calc_distancia(part, centro):
    dist_x = part.pos_x - centro[0]
    dist_y = part.pos_y - centro[1]

    dist = np.sqrt((dist_x*dist_x)+(dist_y*dist_y))
    return dist

def calc_peso(dist):
    return math.exp(-dist)

def media_pesos(lst_particulas):
    sum_peso = 0.0
    for part in lst_particulas:
        sum_peso = sum_peso + part.weight
    return sum_peso/len(lst_particulas)

def getParticle_byWeight(weight,lst_particulas):
    #pegando uma particula na distribuicao pelo seu peso
    if weight >= 1:
        return lst_particulas[NUM_PARTICULAS-1]
    else:
        for i in range(NUM_PARTICULAS):
            if weight >= lst_particulas[i].resample_weights[0] and weight < lst_particulas[i].resample_weights[1]:
                return lst_particulas[i]
            else:
                continue

def copy_particle(part):
    part_nova = particula(part.pos_x,part.pos_y,part.velocity, part.theta)
    part_nova.weight = part.weight
    return part_nova

def initialize_pf(centro):
    lst_particulas = []
    for i in range(NUM_PARTICULAS):
        lst_particulas.append(particula(centro[0],centro[1],random.uniform(V_MIN,V_MAX),random.uniform(-math.pi,math.pi)))
    return lst_particulas
