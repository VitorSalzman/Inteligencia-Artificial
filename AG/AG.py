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

class Cromossomo():
	
    def __init__(self):
        self.bits=[0,0,0,0,0,0,0,0,0,0]
        self.normalizado=0
        self.aptidao=0
       
	def gera_vetor_bits(self)
		for i in range(len(self.bits)):
			self.bits[i] = randint(0,1)
       
       

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))