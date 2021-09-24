from io import open
from os import path
import numpy as np
import json

def carga_db(productos):
    with open("db_productos.txt", "w+") as opfile:
        for i in productos:
            opfile.write(productos[0][0])
        print(productos[0][0])
        

    #with open('db_productos.txt', 'wr') as temp_op:
    #    productos = json.load(temp_op)
    #print(templist)
    #producto = [productos]
    #for i in range(len(productos)):
    #    for j in range(len(productos)):
    
    #        print(i,[0])
    opfile.close()           

def muestra_db():
    if path.isfile('db_productos.txt'):
        archivo = open('texto.txt', 'r')
        textos = archivo.readlines()
        archivo.close()
        print(textos)

    else:
        print('No existe el archivo')

def muestra_catalogory():
    pass
