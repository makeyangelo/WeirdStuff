# -*- coding: utf-8 -*-

import sys

listaColor=[' ', '\xe2','\x96','\x88','\x92','\x91','\n']

def generator(listaColor, cantidadColor, ordenColor):
    for cantidad, color in zip(cantidadColor, ordenColor):
        for numero in range(cantidad):
            sys.stdout.write(listaColor[color])

def counter (listaColor, arte):
    cantidadColor=[]
    ordenColor=[]

    for cod,n in zip(arte,range(len(arte))):
        if n == 0:
            ordenColor.append(listaColor.index(cod))
            cantidadColor.append(1)
        else:
            if arte[n-1] == cod:
                cantidadColor[-1]=cantidadColor[-1]+1
            else:
                cantidadColor.append(1)
                ordenColor.append(listaColor.index(cod))

    return zip(cantidadColor,ordenColor)

def getColorList(arte):
    listaColor=[]
    for c in arte:
        try:
            listaColor.index(c)
        except ValueError:
            listaColor.append(c)
        else:
            None
    return listaColor
        

arte="""        ██████████████████████
      ██████████████████████████       
    ██████████████████████████████     
    ████████████████████████████████  
  ████████▒▒▒▒██████████████████████  
  ██████▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██████████  
  ██████▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒██████████
██████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒████▒▒████
██████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
██████▒▒░░░░▒▒██▒▒▒▒██▒▒░░░░▒▒████████
████████░░░░▒▒▒▒████▒▒▒▒░░░░██████████
████████████▒▒▒▒▒▒▒▒▒▒▒▒██████████████
  ██  ████████████▒▒▒▒██████████  ██  
                ██▒▒▒▒██      ██      """

"""
c,o=zip(*counter(listaColor,arte))
generator(listaColor,c,o)
print('\n')
print(listaColor)
sys.stdout.write("Orden Color: ")
print(o)
sys.stdout.write("Cantidad Color: ")
print(c)
"""

print(getColorList(arte))
