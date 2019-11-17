from random import randint
import math
import random
import xlwt
from xlwt import Workbook

class Cromossomo():

    def __init__(self):
        self.gene = 0
        self.aptidao = 0

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

    def setGene(self,gene):
        self.gene = gene
        self.calc_aptidao()
    
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

# def calc_aptidao(vetCromo):
#     for cromo in vetCromo:
#         b = cromo.calc_aptidao()
#        # print("apt: {} | norm {}".format(b))
#     return vetCromo

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
        print(novovetor_cromossomos[i].getAptidao())
    return novovetor_cromossomos

def crossOver(cromossomos):
    novovetor_cromossomos = [Cromossomo() for _ in range(10)]
    for i in range(0,10,2):  # pula de 2 em 2
        r1 = randint(0, 9)
        r2 = randint(0, 9)
        # poderiamos verificar se é o mesmo numero
        chance = randint(0,100)
        if chance <= globalcross:
            print("CrossOvered - [{},{}]".format(r1,r2))
            B = random.uniform(-A, 1 + A)

            cromo1 = cromossomos[r1]
            cromo2 = cromossomos[r2]

            print("Antes - p1:{}|p2:{}".format(cromo1.getAptidao(), cromo2.getAptidao()))

            C = cromo1.getGene() + B * (cromo2.getGene() - cromo1.getGene())
            C2= cromo2.getGene() + B * (cromo1.getGene() - cromo2.getGene())

            if C < -20:
                C = -20
            if C > 20:
                C = 20
            if C2 < -20:
                C2 = -20
            if C2 > 20:
                C2 = 20

            novovetor_cromossomos[i].setGene(C)
            novovetor_cromossomos[i+1].setGene(C2)

            print("Depois - p1:{}|p2:{}".format(novovetor_cromossomos[i].getAptidao(), novovetor_cromossomos[i+1].getAptidao()))
            print("####################")
        else:
            novovetor_cromossomos[i] = cromossomos[r1]
            novovetor_cromossomos[i + 1] = cromossomos[r2]


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
    print("|---------------START-----------------|")
    for cromo in vetCromo:
        cromo.print()
    print("|---------------END-------------------|")



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

print("População Iniciada")
vetor_cromossomos = [Cromossomo() for _ in range(10)]  # criando 10 cromossomos
for i in vetor_cromossomos:
    i.genes = i.gera_gene()  # parte 1
    i.calc_aptidao()

    print(i.getGene(), i.getAptidao())
print("inicialização finalizada")

# g = 0
# maxg = 1
# printCromo(vetor_cromossomos)
# print("START GENERATION")
# # reservando o elite antes de mudar td
# elite = elitismo(vetor_cromossomos)
# printCromo(vetor_cromossomos)
# print("Torneio")
# vetor_cromossomos = torneio(vetor_cromossomos)
# printCromo(vetor_cromossomos)
# print("CrossOver")
# vetor_cromossomos = crossOver(vetor_cromossomos)
# printCromo(vetor_cromossomos)
# print("Mutation")
# vetor_cromossomos = mutation(vetor_cromossomos,g,maxg)
# # print("Aptidation Times")
# # vetor_cromossomos = calc_aptidao(vetor_cromossomos)
# printCromo(vetor_cromossomos)
# print("Elitismo")
# vetor_cromossomos = add_elite(vetor_cromossomos,elite)
# printCromo(vetor_cromossomos)
# print("END GENERATION ")


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

        print("População Iniciada #########################################################")
        vetor_cromossomos = [Cromossomo() for _ in range(10)]  # criando 10 cromossomos
        for i in vetor_cromossomos:
            i.genes = i.gera_gene()  # parte 1
            i.calc_aptidao()

            print(i.getGene(), i.getAptidao())
        print("inicialização finalizada")

        for i in range(generation):
            print("START GENERATION")
            # reservando o elite antes de mudar td
            elite = elitismo(vetor_cromossomos)
            print("Torneio")
            vetor_cromossomos = torneio(vetor_cromossomos)
            print("CrossOver")
            vetor_cromossomos = crossOver(vetor_cromossomos)
            print("Mutation")
            vetor_cromossomos = mutation(vetor_cromossomos, i, generation)
            print("Elitismo")
            vetor_cromossomos = add_elite(vetor_cromossomos, elite)
            print("print time")
            printCromo(vetor_cromossomos)
            print("END GENERATION ")

            eliteSon = elitismo(vetor_cromossomos)
            if (eliteSon.getAptidao() < -19):
                exit()
            sheet.write(i+y + 1, x+j+1, eliteSon.getAptidao())
    x = 1
    y = 15
wb.save('algoritmo_genetico_table.xls')
