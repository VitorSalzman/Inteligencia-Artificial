import sys
from math import sqrt
from math import pow


# verifica se as coordenadas de inicio e fim estão em um obstaculo ou acima da dimensão
def verificaObstaculo(startEnds):

    for posicoes in startEnds:
        for tupla in posicoes:
            if (tupla[0] > len(matriz)-1 or tupla[1] > len(matriz[0])-1):
                print ('Erro! Dimensões incorretas!')
                return False
            if matriz[tupla[0]][tupla[1]] == '1':
                print("Entrada/Saida inserida em obstaculo, favor inserir coordenada valida")
                return False

    return True

# Dada uma matriz e a posicao atual pelas coordenadas (i,j),
# encontra os estados sucessores com 1 passo de (i,j)
def encontra_estados_sucessores(matriz, posicao_atual): # M e N podem ser extraidos de matriz, ja que são o tamanho maximo em linha e coluna da matriz
    M = int(len(matriz))  # numero de linhas.
    N = int(len(matriz[0]))  # numero de colunas.
    i = posicao_atual[0]
    j = posicao_atual[1]
    estados_sucessores = [] # isso não precisava ser um array
    if i > 0 and matriz[i - 1][j] != '1':  # Move para cima na matriz.
        estados_sucessores.append((i - 1, j))
    if i + 1 < M and matriz[i + 1][j] != '1':  # Move para baixo na matriz.
        estados_sucessores.append((i + 1, j))
    if j > 0 and matriz[i][j - 1] != '1':  # Move para esquerda na matriz.
        estados_sucessores.append((i, j - 1))
    if j + 1 < N and matriz[i][j + 1] != '1':  # Move para direita na matriz.
        estados_sucessores.append((i, j + 1))

    return estados_sucessores

def printa_matriz(mat): # altera a matriz para printa a resposta
    for tupla in mat:
        matriz[tupla[0]][tupla[1]] = '#'
    matriz[mat[0][0]][mat[0][1]] = 'S'
    matriz[mat[-1][0]][mat[-1][1]] = 'E'
    for i in matriz:
        print(i)

# Dado um estado considerado final, uma lista de predecessores e um numero de iteracao,
# apresenta em qual iteracao foi encontrada a solucao e como partir do estado inicial
# e chegar ate o estado final a partir da solucao parcial armazenada em predecessores.

def apresenta_solucao(estado, predecessores, iteracao):
    caminho = []
    caminho.append(estado)
    print("Solucao encontrada na iteracao " + str(iteracao) + ":")
    while predecessores[estado] != None:
        caminho.append(predecessores[estado])
        estado = predecessores[estado]
    caminho = caminho[::-1]
    printa_matriz(caminho)

# Dado um estado qualquer e um conjunto de estados finais,
# calcula a distancia do estado qualquer ate um estado final mais proximo.
def calcula_distancia_meta(estado, estados_finais): # MAHATAN
    x = estado[0]
    y = estado[1]
    distancia_minima = 1000000000

    for estado_final in estados_finais: # para cada estado final (se tiver + de 1) calcula a hipotenusa que é o mahatan
        x_estado_final = estado_final[0]
        y_estado_final = estado_final[1]
        diff1 = x_estado_final - x
        diff2 = y_estado_final - y
        somaDiffs = pow(diff1, 2) + pow(diff2, 2)
        distancia_atual = sqrt(somaDiffs)
        if distancia_atual < distancia_minima:
            distancia_minima = distancia_atual
    return distancia_minima

# Dada uma franja (fringe) e uma funcao heuristica,
# encontra o estado com menor valor nessa franja.
def encontra_estado_mais_promissor(franja, heuristica_estados):
    valor_mais_promissor = 1000000000
    indice_mais_promissor = 0
    indice = 0
    for estado in franja:
        if heuristica_estados[estado] < valor_mais_promissor:
            valor_mais_promissor = heuristica_estados[estado]
            indice_mais_promissor = indice
        indice = indice + 1
    return indice_mais_promissor




# Algoritmo: Busca A* (A Estrela / A Star)
def busca_a_estrela(matriz, estado_inicial, estados_finais):

    distancia_meta = {}
    distancia_percorrida = {}
    heuristica = {}
    predecessores = {}
    estados_expandidos = []
    solucao_encontrada = False

    print("Algoritmo: A* (A Estrela)")

    # Inicializacao de distancia percorrida (f), distancia ate a meta (g) e heuristica (h = f+g).
    distancia_percorrida[estado_inicial] = 0                                                                # o quanto andou
    distancia_meta[estado_inicial] = calcula_distancia_meta(estado_inicial, estados_finais)                 # a distancia mahatan pro destino
    heuristica[estado_inicial] = distancia_percorrida[estado_inicial] + distancia_meta[estado_inicial]      # a soma dos 2 para definir a heuristica
    predecessores[estado_inicial] = None                                                                    # não tem pq acabou de iniciar
    print ("Heuristica da Distancia no Estado Inicial: " + str(heuristica[estado_inicial]))
    franja = []
    franja.append(estado_inicial)
    iteracao = 1
    while len(franja) != 0:
        indice_mais_promissor = encontra_estado_mais_promissor(franja, heuristica)
        estado = franja.pop(indice_mais_promissor)
        if estado in estados_finais:
            solucao_encontrada = True
            break
        estados_sucessores = encontra_estados_sucessores(matriz, estado)                                    # estados que não são parede
        estados_expandidos.append(estado)

        for sucessor in estados_sucessores:
            if sucessor not in estados_expandidos and sucessor not in franja:
                franja.append(sucessor)
                if sucessor not in heuristica.keys():
                    distancia_meta[sucessor] = calcula_distancia_meta(sucessor, estados_finais)
                    distancia_percorrida[sucessor] = distancia_percorrida[estado] + 1
                    heuristica[sucessor] = distancia_meta[sucessor] + distancia_percorrida[sucessor]
                    predecessores[sucessor] = estado
        iteracao = iteracao + 1

    if solucao_encontrada == True:
        apresenta_solucao(estado, predecessores, iteracao)
    else:
        print("Nao foi possivel encontrar uma solucao para o problema.")


def leitura_txt(arquivo):
    file = open(arquivo, 'r')
    matriz = []
    for line in file:
        matrizLine = []
        for c in line:
            if c != "\n" and c != " ":
                matrizLine.append(c)
        matriz.append(matrizLine)
        print(matrizLine)

    return matriz

if len(sys.argv) == 2:

    matriz = leitura_txt(sys.argv[1])

    # receber por scanner os estados iniciais e finais

    estado_inicial = input("Enter the (x,y) coordinates to Start: ")
    estado_inicial = [tuple(int(x) for x in estado_inicial.split(" "))]
    estados_finais = input("Enter the (x,y) coordinates to End: ")
    estados_finais = [tuple(int(x) for x in estados_finais.split(" "))]

    if verificaObstaculo([estado_inicial, estados_finais]):
        print("Matriz (mapa): ")
        for i in matriz:
            print(i)
        print("Estado Inicial: " + str(estado_inicial))
        print("Estado Final: " + str(estados_finais))
        busca_a_estrela(matriz, estado_inicial[0], estados_finais)
else:
    print("Forneca um arquivo CSV para os algoritmos de busca.")
