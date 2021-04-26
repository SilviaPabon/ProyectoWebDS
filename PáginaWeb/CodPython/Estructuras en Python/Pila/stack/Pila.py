# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:14:39 2021

@author: DAVID LEONARDO
"""


class Pila(object):

#--------alberga elementos de la pila-------#
    def __init__(self):
        self.items=[]
        

#--------Es vacia--------------#
    def isEmpty(self):
        return len(self.items)==0

#---------tamaño------------#

    def size(self):
        return len(self.items)

#--------Elimina por la cabeza---------------#
    def pop(self):
        dato=None
        if not self.isEmpty():
            dato=self.items.pop()
        return dato

#-----------verl el ultimo dato sin elimnarlo---------#
    def peek(self):
        dato=None
        if not self.isEmpty():
            dato=self.items[len(self.items)-1]
        return dato

#-------------insertar dato---------------#
    def push(self, dato):
        self.items.append(dato)

#-----------Apilar--------------------------#
    def apliar(self, dato):
        self.items.append(dato)
        print("Actualizado: ", self.items)

#-----------Extrae elementos---------------#
    def desapilar(self):
        if self.esVacia():
            return None 
        else:
            return self.items.pop()

#--------------Verifica si la pila tiene valor 0 -----------#

    def esVacia(self):
        if len(self.items)==0:
            return True 
        else:
            return False

#--------Limpia la pila-----------#
    def vaciar(self):
        return self.items.clear()


#--------------Muestra los datos---------#
    def imprimirPila(self):
        print(self.items)
    
    
    def getDato(self, pos):
        return self.items[pos]
        