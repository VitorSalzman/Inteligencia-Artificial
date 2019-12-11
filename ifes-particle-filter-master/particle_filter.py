from particle import particula
import numpy as np
import random
import math
import pf_tools as pft
from pf_tools import NUM_PARTICULAS , V_MIN, V_MAX, STD_DEV_V, STD_DEV_T, DELTA_TIME


def motion_model(delta_time, particula):

    new_theta = particula.theta + np.random.normal(0.0,STD_DEV_T)

    new_velocity = particula.velocity + np.random.normal(0.0,STD_DEV_V)
    if (new_velocity > V_MAX):
        new_velocity = V_MAX
    elif (new_velocity < V_MIN):
        new_velocity = V_MIN

    new_x = particula.pos_x + (particula.velocity * delta_time * math.cos(particula.theta))
    new_y = particula.pos_y + (particula.velocity * delta_time * math.sin(particula.theta))

    particula.pos_x = int(new_x)
    particula.pos_y = int(new_y)
    particula.velocity = new_velocity
    particula.theta = new_theta

    return particula


def observation_model(lst_particulas,centro):
    sum_peso = 0.0

    #calculando o peso de cada particula
    for part in lst_particulas:
        w = pft.calc_peso(pft.calc_distancia(part,centro))
        part.weight = w
        sum_peso = sum_peso + w

    #Normalizando o peso de cada partiula
    for part in lst_particulas:
        part.weight = part.weight/sum_peso

    return lst_particulas


def resample(lst_particulas):
    #Definindo o vetor de distribuicao de probabilidade
    for i in range(NUM_PARTICULAS):
        #definindo as fronteiras de cada particula na distribuicao
        if i == 0:
            lst_particulas[i].resample_weights = (0,lst_particulas[i].weight)
        else:
            lst_particulas[i].resample_weights = (lst_particulas[i-1].resample_weights[1],lst_particulas[i-1].resample_weights[1]+lst_particulas[i].weight)

    #Primeira particula selecionada aleatoriamente com um peso aleatorio de referencia
    referencia = random.random()

    #media dos pesos
    k = pft.media_pesos(lst_particulas)

    new_sample = []
    for i in range(NUM_PARTICULAS):
        #Operacao para tornar a lista circular
        if referencia > 1:
            referencia = referencia - 1
        #Funcao getParticle_byWeight para buscar a particula
        #Funcao copy para fazer uma copia da particular e adicionala a uma nova amostra
        nova_particula = pft.copy_particle(pft.getParticle_byWeight(referencia,lst_particulas))
        new_sample.append(nova_particula)
        referencia = referencia + k

    return new_sample


def filtro_de_particulas(centro,lst_particulas):
    #Modelo de Movimento
    for i in range(NUM_PARTICULAS):
        lst_particulas[i] = motion_model(DELTA_TIME,lst_particulas[i])

    #Modelo de Observacao
    lst_particulas = observation_model(lst_particulas,centro)

    #Re-amostragem
    lst_particulas = resample(lst_particulas)
    return lst_particulas
