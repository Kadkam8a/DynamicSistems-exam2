#!/usr/bin/env python3
#
#
#    Copyright (C) 2022
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import numpy as np
import math
import matplotlib.pyplot as plt


def square(x0,y0,L):
    Puntos=[[],[]]
    Puntos[0].append(x0)
    Puntos[1].append(y0)
    #^ 
    Puntos[0].append(x0)
    Puntos[1].append(y0+L)
    #>
    Puntos[0].append(x0+L)
    Puntos[1].append(y0+L)
    #V
    Puntos[0].append(x0+L)
    Puntos[1].append(y0)
    #< repetir para cerrar el cuadrado
    Puntos[0].append(x0)
    Puntos[1].append(y0)
    return Puntos

def fractal(X,Y,N,L,AX,Excepto):
    X, Y = square(X,Y,L)
    ax.plot(X,Y)
    if N > 0:
        L0X=X[0]
        L0Y=Y[0]
        
        L1X=X[1]
        L1Y=Y[1]
        
        L2X=X[2]
        L2Y=Y[2]
        
        L3X=X[3]
        L3Y=Y[3]

        #izquierda
        if(Excepto!=0):
            C0X=L0X-L/3
            C0Y=L0Y+L/3
            fractal(C0X,C0Y,N-1,L/3,AX,1) #no dibujar a la derecha
        #derecha
        if(Excepto!=1):
            C0X=L0X+L
            C0Y=L0Y+L/3
            fractal(C0X,C0Y,N-1,L/3,AX,0) #no dibujar a la izquierda
        
        #arriba
        if(Excepto!=2):
            C0X=L0X+L/3
            C0Y=L0Y+L
            fractal(C0X,C0Y,N-1,L/3,AX,3) #no dibujar abajo
        
        #abajo
        if(Excepto!=3):
            C0X=L0X+L/3
            C0Y=L0Y-L/3
            fractal(C0X,C0Y,N-1,L/3,AX,2) #no dibujar arriba
        
        

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')

fractal(0,0,6,1,ax,-1)
plt.show()
