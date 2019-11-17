from random import randint
import math
import random
import xlwt
from xlwt import Workbook

class Cromossomo():

    def __init__(self):
        self.gene = 0
        self.aptidao = None

    def gera_gene(self):
        self.gene = random.uniform(-20,20)

    def mutation(self,g,gmax):
        genes = self.gene
        chance = randint(0, 100)
        if chance <= globalmutation:
            print("MUTOU!")
            print("antes:{}", genes)
            r1 = random.random()
            r2 = random.random()
            b = 20
            a = -20
            f = pow((r2*(1-(g/gmax))),20)

            if (r1 >= 0.5):
                c = genes +(b-genes) * f
            else:
                c = genes -(genes-a) * f

            genes = c

            print("depois:{}",genes)

        self.gene = genes

    def calc_aptidao(self):
        x = self.gene
        cos = math.cos(x)
        apt = cos * x + 2
        self.aptidao = apt
        return self.aptidao


    
    def getGene(self):
        return self.gene
    def getAptidao(self):
        return self.aptidao

    def print(self):
        print("genes: {} | apti: {}".format(self.gene,self.aptidao))

def mutation(vetCromo,g,gmax):
    for cromo in vetCromo:
        cromo.mutation(g,gmax)
    return vetCromo

def calc_aptidao(vetCromo):
    for cromo in vetCromo:
        b = cromo.calc_aptidao()
       # print("apt: {} | norm {}".format(b))
    return vetCromo

def torneio(cromossomos):
    novovetor_cromossomos = [Cromossomo() for _ in range(10)]
    for i in range(10): # tamanho do vetor de genes
        r1 = randint(0, 9)
        r2 = randint(0, 9)
        #poderiamos verificar se é o mesmo numero
        print(r1, r2)
        print(cromossomos[r1].aptidao, cromossomos[r2].aptidao)
        if cromossomos[r1].getAptidao() > cromossomos[r2].getAptidao():
            novovetor_cromossomos[i] = (cromossomos[r2])
        else:
            novovetor_cromossomos[i] = (cromossomos[r1])
    # print(novovetor_cromossomos[i].genes)
    return novovetor_cromossomos

def crossOver(cromossomos):
    novovetor_cromossomos = [Cromossomo() for _ in range(10)]
    for i in range(0,10,2):  # pula de 2 em 2
        r1 = randint(0, 9)
        r2 = randint(0, 9)
        # poderiamos verificar se é o mesmo numero
        chance = randint(0,100)
        if chance <= globalcross:

            B = random.uniform(-A, 1 + A)

            cromo1 = cromossomos[r1].getGene()
            cromo2 = cromossomos[r2].getGene()

            print("Antes")
            print("p1:{}|p2:{}".format(cromo1, cromo2))

            C = cromo1 + B * (cromo2 - cromo1)
            C2= cromo2 + B * (cromo1 - cromo2)

            novovetor_cromossomos[i].gene = C
            novovetor_cromossomos[i+1].gene = C2

            print("Depois")
            print("p1:{}|p2:{}".format(novovetor_cromossomos[i].getGene(), novovetor_cromossomos[i+1].getGene()))
            print("####################")

    return novovetor_cromossomos

def elitismo(vetCromo):
    minimo = math.inf
    for cromo in vetCromo:
        if cromo.getAptidao() <= minimo:
            elite = cromo
            minimo = cromo.getAptidao()
    print("ELITE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    elite.print()
    return elite

def add_elite(vetCromo,elite):
    maximo = -math.inf
    for i in range(len(vetCromo)):
        if vetCromo[i].getAptidao() >= maximo:
            DS = i # pos dark sheep
            maximo = vetCromo[i].getAptidao()

    vetCromo[DS] = elite
    print("pos DS:",DS)
    return vetCromo


def printCromo(vetCromo):
    for cromo in vetCromo:
        cromo.print()



###########################################
# INICIO CODIGO
###########################################

global globalmutation
global globalcross
global A

A = 0.5
globalmutation = 1
globalcross = 80
maxGeneration = [10,20]
interations = 10


'''vetor_cromossomos = [Cromossomo() for _ in range(10)]  # criando 10 cromossomos
for i in vetor_cromossomos:
    i.genes = i.gera_gene()  # parte 1
    i.calc_aptidao()

    # print(i.genes, i.aptidao)
    
print("START GENERATION")
# reservando o elite antes de mudar td
elite = elitismo(vetor_cromossomos)
print("Torneio")
vetor_cromossomos = torneio(vetor_cromossomos)
print("CrossOver")
vetor_cromossomos = crossOver(vetor_cromossomos)
print("Mutation")
vetor_cromossomos = mutation(vetor_cromossomos)
print("Aptidation Times")
vetor_cromossomos = calc_aptidao(vetor_cromossomos)
print("Elitismo")
vetor_cromossomos = add_elite(vetor_cromossomos,elite)
print("print time")
printCromo(vetor_cromossomos)
print("END GENERATION ")
'''

wb = Workbook()
sheet = wb.add_sheet('algoritmo_genetico_table')
x = 1
y = 1

for generation in maxGeneration:

    for i in range(generation):
        sheet.write(i+y+1, x, 'gen-{}'.format(i + 1))

    for i in range(interations):
        sheet.write(y, i+x+1, 'int-{}'.format(i + 1))

    for j in range(interations):

        vetor_cromossomos = [Cromossomo() for _ in range(10)]  # criando 10 cromossomos
        for i in vetor_cromossomos:
            i.genes = i.gera_gene()  # parte 1
            i.calc_aptidao()

            print(i.genes, i.aptidao)

        for i in range(generation):
            print("START GENERATION")
            # reservando o elite antes de mudar td
            elite = elitismo(vetor_cromossomos)
            print("Torneio")
            vetor_cromossomos = torneio(vetor_cromossomos)
            print("CrossOver")
            vetor_cromossomos = crossOver(vetor_cromossomos)
            print("Mutation")
            vetor_cromossomos = mutation(vetor_cromossomos,i,generation)
            print("Aptidation Times")
            vetor_cromossomos = calc_aptidao(vetor_cromossomos)
            print("Elitismo")
            vetor_cromossomos = add_elite(vetor_cromossomos,elite)
            print("print time")
            printCromo(vetor_cromossomos)
            print("END GENERATION ", i)

            eliteSon = elitismo(vetor_cromossomos)
            sheet.write(i+y + 1, x+j+1, eliteSon.getAptidao())
    x = 1
    y = 15

wb.save('algoritmo_genetico_table.xls')
