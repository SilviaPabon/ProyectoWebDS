# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:13:30 2021

@author: DAVID LEONARDO
"""

#%%------------------C O L A  E S T A T I C A----------------%%#

class cola:
    __sizeCola= int(0)
    __ColaList=[]
    
    def __init__(self, sizeCola):
        self.__sizeCola= sizeCola
        

#------------insertar dato-------------------#
    def insertar(self,dato):
        if self.ColaTop():
            return False
        else:
            self.__ColaList.append(dato)

#-------------eliminar dato-----------------#
    def remove(self):
        if self.isEmpty():
            return False
        else: 
            return self.__ColaList.pop(0)
        
#-------------Es vacia----------------------#
    def isEmpty(self):
        if len(self.__ColaList)==0:
            return True
        else:
            return False

#-----------Cola llena----------------------#
    def isFull(self):
        if self.__sizeCola==len(self.__ColaList):
            return True
        else:
            return False

#------------Limpiar------------------------#
    def clearr(self):
        self.__ColaList.clear()
        
#------------Tamaño-------------------------#
    def size(self):
        return len(self.__ColaList)
    

#%%----------------C O L A   D I N A M I C A----------------------

class ColaDinamica:
    __sizeCola=int(0)
    __ColaLista=[]
    
    def insertar(self, dato):
        self.__ColaLista.append(dato)
        return True
    
    def remove(self):
        if self.isEmpty():
            return False
        else:
            return self.__ColaLista.pop(0)
        
    def isEmpty(self):
        if len(self.__ColaLista)==0:
            return True
        else:
            return False
    