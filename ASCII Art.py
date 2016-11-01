# -*- coding: utf-8 -*-

import sys

#listaColor->Contains each type of character the art is composed of.
#cantidadColor->Contains how much of that character there are in succesion.
#ordenColor->Contains the index of the character in listaColor
#cantidadColor and ordenColor are the same size. ordenColor tells wich character to use and cantidadColor how much of it tu use.

#Use the lists to print the art.
def generator(listaColor, cantidadColor, ordenColor):
    for cantidad, color in zip(cantidadColor, ordenColor):
        for numero in range(cantidad):
            sys.stdout.write(listaColor[color])

#Get the sequence of quantity and characters.
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

#Get all the character types the art is made of.
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
        
def example():
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
    listaColor=getColorList(arte)
    c,o=zip(*counter(listaColor,arte))#zip(*zippedStuff) unzips what has been zipped
    generator(listaColor,c,o)
    print('\n\n')
    print("listaColor used:")
    print(listaColor)
    sys.stdout.write("Orden Color: ")
    print(o)
    sys.stdout.write("Cantidad Color: ")
    print(c)
