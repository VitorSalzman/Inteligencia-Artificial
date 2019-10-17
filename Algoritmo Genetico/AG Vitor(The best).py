#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  teste.py
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

	
def conversor_b_d(vet):
	soma=0
	for i in range(len(vet)):
		if vet[len(vet)-i-1]==1: 
			soma += 2**i
	return soma
	
def normaliza(vet):
	b10 = conversor_b_d(vet)
	l=len(vet)
	minimo = -20.0
	maximo = 20.0
	x = minimo +( maximo - minimo) *(b10/((2**l)-1))		
	return x
	
class Cromossomo():
	
	def __init__(self):
		self.bits=[0,0,0,0,0,0,0,0,0,0]
		self.normalizado=0
		self.aptidao=0
	
	def gera_vetor_bits(self):
		newcromo=[]
		for i in range(len(self.bits)):
			newcromo.append(randint(0,1))
		return newcromo
	
		
		
		
vetor_cromossomos= [Cromossomo() for _ in range(10)] # criando 10 cromossomos
cromo = Cromossomo()
for i in vetor_cromossomos:          #parte 1
	i.bits=i.gera_vetor_bits()
	i.normalizado=normaliza(i.bits)
	print(i.normalizado)
	
	'''
print("teste binario decimal")
	
print(conversor_b_d(vetor_cromossomos[0].bits))	
print(normaliza([1,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1]))	#teste vetor do slide
   '''


