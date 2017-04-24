# -*- coding: utf-8 -*-

import ArbolB

class NodoLista():

    def __init__(self):
        self.nombre=""
        self.contrasenia=""
        self.siguiente=None
        self.anterior=None
        self.carpeta=None


class Lista():

    def __init__(self):
        self.primero=None
        self.ultimo=None


    def Insertar(self,nombre,contrasenia):
        if self.primero==None:
            nuevo=NodoLista()
            nuevo.nombre=nombre
            nuevo.contrasenia=contrasenia
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            auxiliar=self.primero
            while auxiliar.siguiente!=None:
                auxiliar=auxiliar.siguiente
            nuevo=NodoLista()
            nuevo.nombre=nombre
            nuevo.contrasenia=contrasenia
            nuevo.anterior=self.ultimo
            auxiliar.siguiente=nuevo
            self.ultimo=nuevo



    def buscar(self,nombre,dato):
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.nombre==nombre:
                Ar=ArbolB.ArbolB()
                auxiliar.carpeta=ArbolB.NodoArbolB()
                auxiliar.carpeta.claves.append(dato)
                Ar.raiz=auxiliar.carpeta
                #Ar.InsertarB(None,Ar.raiz,dato)
            auxiliar=auxiliar.siguiente

lis=Lista()
lis.Insertar("mario",123)
lis.Insertar("roberto",456)
lis.Insertar("cojolon",2404)
lis.buscar("mario",24)
lis.buscar("mario",25)
Ar=ArbolB.ArbolB()
print(Ar.raiz)
