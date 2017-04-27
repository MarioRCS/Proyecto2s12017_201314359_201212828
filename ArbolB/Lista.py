# -*- coding: utf-8 -*-

import MDispersa

import AVL

class NodoLista:
    def __init__(self,nombre,indice):
        self.nombre=nombre
        self.indice=indice
        self.siguiente=None
        self.AVL=None
        self.arbol=None
        self.temp=None

class Lista:
    def __init__(self):
        self.primero=None

    def insertar(self,nombre,indice):
        if self.primero==None:
            nuevo=NodoLista(nombre,indice)
            self.primero=nuevo
            nuevo.siguiente=None
        else:
            auxiliar=self.primero
            while auxiliar.siguiente!=None:
                auxiliar=auxiliar.siguiente
            nuevo=NodoLista(nombre,indice)
            auxiliar.siguiente=nuevo

    def Login(self,nombre,indice):
        acceso=False
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.nombre==nombre:
                if auxiliar.indice==indice:
                    acceso=True
            auxiliar=auxiliar.siguiente
        return acceso

    def GraficarLista(self):
        texto="digraph g{\n"
        auxiliar=self.primero
        while auxiliar!=None:
            texto+="l"+str (auxiliar.nombre)+str (auxiliar.indice)+'[label="'+str(auxiliar.nombre)+'"]; \n'
            auxiliar=auxiliar.siguiente
        auxiliar2=self.primero
        while auxiliar2.siguiente!=None:
            texto+="l"+str (auxiliar2.nombre)+str (auxiliar2.indice)+" -> "+"l"+str (auxiliar2.siguiente.nombre)+str (auxiliar2.siguiente.indice)+"; \n"
            auxiliar2=auxiliar2.siguiente
        texto+="}"
        return texto

    def BuscarArbol(self,indice):
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.indice==indice:
                if auxiliar.AVL!=None:
                    ar=AVL.Arbol()
                    texto=ar.GraficarArbol(auxiliar.AVL)
            auxiliar=auxiliar.siguiente
        return texto

    def InsertAVL_in_List(self,indice,dato):
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.indice==indice:
                if auxiliar.AVL==None:
                    ar=AVL.Arbol()
                    auxiliar.AVL=AVL.NodoArbol(dato)
                    #ar.PosOrden(auxiliar.AVL)
                else:
                    ar=AVL.Arbol()
                    ar.InsertarAVL(auxiliar.AVL,dato)
                    ar.PosOrden(auxiliar.AVL)
                    if auxiliar.AVL.factor==2:
                        if auxiliar.AVL.izquierdo.factor==1:
                            n=auxiliar
                            n1=auxiliar.AVL
                            n2=auxiliar.AVL.izquierdo
                            n1.izquierdo=n2.derecho
                            n2.derecho=n1
                            n.AVL=n2
                        elif auxiliar.AVL.izquierdo.factor==-1:
                            p=auxiliar
                            n=auxiliar.AVL
                            n1=auxiliar.AVL.izquierdo
                            n2=auxiliar.AVL.izquierdo.derecho
                            n1.derecho=n2.izquierdo
                            n2.izquierdo=n1
                            n.izquierdo=n2.derecho
                            n2.derecho=n
                            p.AVL=n2
                    elif auxiliar.AVL.factor==-2:
                        if auxiliar.AVL.derecho.factor==-1:
                            p=auxiliar
                            n=auxiliar.AVL
                            n1=auxiliar.AVL.derecho
                            n.derecho=n1.izquierdo
                            n1.izquierdo=n
                            p.AVL=n1
                        elif auxiliar.AVL.derecho.factor==1:
                            p=auxiliar
                            n=auxiliar.AVL
                            n1=auxiliar.AVL.derecho
                            n2=auxiliar.AVL.derecho.izquierdo
                            n1.izquierdo=n2.derecho
                            n2.derecho=n1
                            n.derecho=n2.izquierdo
                            n2.izquierdo=n
                            p.AVL=n2
            auxiliar=auxiliar.siguiente




