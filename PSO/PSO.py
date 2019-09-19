#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PSO.py
#  
#  Copyright 2019 20161BSI0403 <20161BSI0403@SR6733>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from random import randint

	
xy=[0,0]	
	
"""
class Particle():
    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 512,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 512])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0])

    def move(self):
        self.position = self.position + self.velocity
"""

def gera_velocidade():
		velocidade=[randint(-77,77),randint(-77,77)]
		return velocidade
		
class Particle():	
	velocidade=[0,0]
	posicao=[0,0]
	def _init_(self):
		self.posicao=xy
		self.fitnes=0
		self.velocidade=[0,0]
	def movimenta(self):
		self.posicao = self.posicao + self.velocidade
		
	def printaposicao(self):
		print("%d %d",self.posicao[0],self.posicao[1])	
	
def inicializa_P(particles,v):
	lista=[particles]
	print("aqui")
	for i in range(particles):
		xy[0]=randint(-512,512)
		xy[1]=randint(-512,512)
		p=Particle()
		print("aqui")
		p.velocidade[0]=v[0]
		p.velocidade[1]=v[1]
		p.printaposicao
		lista.append(p)
	return lista		
		
		                              
def main(args):
	
	P = int(args[1])#Número de partículas
	iterations=int(args[2])#Número de interações
	
	list_P = [P]
	v=gera_velocidade()
	list_P=inicializa_P(P,v)
	print("aqui")
	
	
	
	#for i in range(P):
		#print(list_P[i].printaposicao)
		#list_P[i].printaposicao(list_P[i])

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
