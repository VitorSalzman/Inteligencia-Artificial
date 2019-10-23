from random import randint
import math
import xlwt
from xlwt import Workbook

class Cromossomo():

    def __init__(self):
        self.bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.normalizado = 0
        self.aptidao = 0

    def gera_vetor_bits(self):
        newcromo = []
        for i in range(len(self.bits)):
            newcromo.append(randint(0, 1))
        return newcromo

    def mutation(self):
        bits = self.bits
        for i in range(len(bits)):
            chance = randint(0, 100)
            if chance <= globalmutation:
                print("MUTOU! pos:", i)
                print("antes:{}", bits)
                if bits[i] == 0:
                    bits[i] = 1
                elif bits[i] == 1:
                    bits[i] = 0
                print("depois:{}",bits)

        self.bits = bits

    def crossOver(self,pos,vetBin):
        self.bits[pos:] = vetBin[pos:]

    def calc_aptidao(self):
        x = self.normalizado
        cos = math.cos(x)
        apt = cos * x + 2
        self.aptidao = apt
        return self.aptidao

    def normaliza(self):
        vet = self.bits
        b10 = conversor_b_d(vet)
        l = len(vet)
        minimo = -20.0
        maximo = 20.0
        x = minimo + (maximo - minimo) * (b10 / ((2 ** l) - 1))
        self.normalizado = x
        return self.normalizado

    def getBits(self):
        return self.bits
    def getNormalizado(self):
        return self.normalizado
    def getAptidao(self):
        return self.aptidao

    def print(self):
        print("bits: {} | apti: {}".format(self.bits,self.aptidao))

def mutation(vetCromo):
    for cromo in vetCromo:
        cromo.mutation()
    return vetCromo

def calc_aptidao(vetCromo):
    for cromo in vetCromo:
        a = cromo.normaliza()
        b = cromo.calc_aptidao()
        print("apt: {} | norm {}".format(b,a))
    return vetCromo

def conversor_b_d(vet):
    soma = 0
    for i in range(len(vet)):
        if vet[len(vet) - i - 1] == 1:
            soma += 2 ** i
    return soma

def torneio(cromossomos):
    novovetor_cromossomos = [Cromossomo() for _ in range(10)]
    for i in range(10): # tamanho do vetor de bits
        r1 = randint(0, 9)
        r2 = randint(0, 9)
        #poderiamos verificar se é o mesmo numero
        print(r1, r2)
        print(cromossomos[r1].aptidao, cromossomos[r2].aptidao)
        if cromossomos[r1].getAptidao() > cromossomos[r2].getAptidao():
            novovetor_cromossomos[i] = (cromossomos[r2])
        else:
            novovetor_cromossomos[i] = (cromossomos[r1])
    # print(novovetor_cromossomos[i].bits)
    return novovetor_cromossomos

def crossOver(cromossomos):
    novovetor_cromossomos = [Cromossomo() for _ in range(10)]
    for i in range(0,10,2):  # pula de 2 em 2
        r1 = randint(0, 9)
        r2 = randint(0, 9)
        # poderiamos verificar se é o mesmo numero
        chance = randint(0,100)
        if chance <= globalcross:
            crop =  randint(1, 8) #aonde q entra a linha de corte
            cromo1 = cromossomos[r1].bits
            cromo2 = cromossomos[r2].bits

            print("Antes")
            print("p1:{}|p2:{}".format(cromo1[:crop],cromo1[crop:]))
            print("p1:{}|p2:{}".format(cromo2[:crop],cromo2[crop:]))

            aux = cromo1.copy()
            aux[crop:] = cromo2[crop:].copy()
            # print("p1:",aux[:crop],"|p2:",aux[crop:])

            novovetor_cromossomos[i].bits = aux

            aux = cromossomos[r2].bits.copy()
            aux[crop:] = cromo1[crop:].copy()
            # print("p1:",aux[:crop],"|p2:",aux[crop:])

            novovetor_cromossomos[i+1].bits = aux

            print("Depois")
            print("p1:{}|p2:{}".format(novovetor_cromossomos[i].bits[:crop], novovetor_cromossomos[i].bits[crop:]))
            print("p1:{}|p2:{}".format(novovetor_cromossomos[i+1].bits[:crop], novovetor_cromossomos[i+1].bits[crop:]))
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

globalmutation = 1
globalcross = 80
maxGeneration = [10,20]
interations = 10


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
            i.bits = i.gera_vetor_bits()  # parte 1
            i.normaliza()
            i.calc_aptidao()

            print(i.bits, i.aptidao)

        for i in range(generation):
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
            print("END GENERATION ", i)

            eliteSon = elitismo(vetor_cromossomos)
            sheet.write(i+y + 1, x+j+1, eliteSon.getAptidao())
    x = 1
    y = 15
wb.save('algoritmo_genetico_table.xls')
