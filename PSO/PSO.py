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

def inicializa_P(particles):
	lista=[particles]
	for i in range(particles):
		lista.append(randint(-512,512))
	return particles	


def main(args):
	
	P = int(args[1])
	list_P = [P]
	
	list_P=inicializa_P(P)
	
	for i in range(P):
		print("aqui")
		print(list_P[i])
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
