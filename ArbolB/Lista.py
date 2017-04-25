# -*- coding: utf-8 -*-

from ArbolB import ArbolB,NodoArbolB

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
        self.raiz=None


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
                Ar=ArbolB()
                Ar.InsertarB(None,Ar.raiz,dato)
            auxiliar=auxiliar.siguiente


