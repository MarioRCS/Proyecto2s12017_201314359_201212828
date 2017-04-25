# -*- coding: utf-8 -*-

class NodoArbolB():
    def __init__(self):
        self.claves=[]
        self.ramas=[]
        self.ramas.append(None)
        self.ramas.append(None)
        self.ramas.append(None)
        self.ramas.append(None)
        self.ramas.append(None)
        self.Numdatos=0
        self.arbolB=None
        self.AVL=None
        self.padre=None


class NodoLista():

    def __init__(self):
        self.siguiente=None
        self.anterior=None
        self.nombre=""
        self.contrasenia=""
        self.carpeta=None



class ArbolB():
    def __init__(self):
        self.raiz=None
        self.primero=None
        self.ultimo=None

    def size(self,claves):
        index=0
        while numero[index]!=None:
            index+=1
        return index

    def InsertarUsuario(self,nombre,contrasenia):
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


    def estalleno(self,pagina):
        lleno=False
        if len(pagina.claves)==4:
            lleno=True
        return lleno


    def ReacomodarRamas(self,pagina,padre,pagina2,dato):
        if self.estalleno(padre):
            padre.claves.append(dato)
            padre.claves.sort()
            padre.ramas.append(None)
            index=len(padre.claves)
            while index > 1 and padre.claves[index-1] > dato:
                padre.ramas[index]=padre.ramas[index-1]
                index-=1
            padre.ramas[index]=pagina2
            temp=padre.claves[2]
            self.Subir(padre,temp)
            padre.ramas.pop()
            padre.ramas.pop()
            padre.ramas.pop()
        else:
            if dato < padre.claves[0]:
                padre.claves.append(dato)
                padre.claves.sort()
                index=len(padre.claves)
                while index > 1:
                    padre.ramas[index]=padre.ramas[index-1]
                    index-=1
                padre.ramas[1]=pagina2
            else:
                padre.claves.append(dato)
                padre.claves.sort()
                if pagina!=self.raiz:
                    padre.ramas.append(None)
                #aqui me quede
                index=len(padre.claves)
                while index > 0:
                    if padre.claves[index-1]==dato:
                        padre.ramas[index]=pagina2
                    index-=1



    def Subir(self,pagina,dato):
        if len(pagina.claves)==4:
            pagina.claves.append(dato)
            pagina.claves.sort()
            temp=pagina.claves[2]
            pagina2=NodoArbolB()
            pagina2.claves.append(pagina.claves[3])
            pagina2.claves.append(pagina.claves[4])
            pagina.claves.pop()
            pagina.claves.pop()
            pagina.claves.pop()
            self.ReacomodarRamas(pagina,pagina.padre,pagina2,temp)
        elif len(pagina.claves)==5:
            temp=pagina.claves[2]
            #print(temp)
            pagina2=NodoArbolB()
            pagina2.claves.append(pagina.claves[3])
            pagina2.claves.append(pagina.claves[4])
            pagina.claves.pop()
            pagina.claves.pop()
            pagina.claves.pop()
            pagina2.ramas.pop()
            pagina2.ramas.pop()
            pagina2.ramas.pop()
            pagina2.ramas.pop()
            pagina2.ramas.pop()
            pagina2.ramas.append(pagina.ramas[3])
            pagina2.ramas.append(pagina.ramas[4])
            pagina2.ramas.append(pagina.ramas[5])
            if pagina==self.raiz:
#                self.InsertarB(None,self.raiz,temp)
                nuevo=NodoArbolB()
                nuevo.claves.append(temp)
                nuevo.ramas[0]=pagina
                nuevo.ramas[1]=pagina2
                self.raiz=nuevo
            else:
                self.ReacomodarRamas(pagina,pagina.padre,pagina2,temp)
        else:
            pagina.claves.append(dato)
            pagina.claves.sort()

    def InsertarB(self,padre,pagina,dato):
        if pagina==self.raiz:
            if pagina==None:
                self.raiz=NodoArbolB()
                self.raiz.claves.append(dato)
            else:
                if dato < self.raiz.claves[0]:
                    if self.raiz.ramas[0]!=None:
                        self.InsertarB(self.raiz,self.raiz.ramas[0],dato)
                    else:
                        if self.estalleno(self.raiz):
                            #dividir Nodo y asignar nueva raiz
                            self.raiz.claves.append(dato)
                            self.raiz.claves.sort()
                            nuevo=NodoArbolB()
                            nuevo.claves.append(self.raiz.claves[2])
                            nuevo.ramas[0]=self.raiz
                            otrapagina=NodoArbolB()
                            otrapagina.claves.append(self.raiz.claves[3])
                            otrapagina.claves.append(self.raiz.claves[4])
                            self.raiz.claves.pop()
                            self.raiz.claves.pop()
                            self.raiz.claves.pop()
                            nuevo.ramas[1]=otrapagina
                            self.raiz=nuevo
                        else:
                            self.raiz.claves.append(dato)
                            self.raiz.claves.sort()
                else:
                    index=len(self.raiz.claves)
                    while dato < self.raiz.claves[index-1] and index > 0:
                        index-=1
                    if index > 0:
                        if self.raiz.ramas[index]!=None:
                            self.InsertarB(self.raiz,self.raiz.ramas[index],dato)
                        else:
                            if self.estalleno(self.raiz):
                                #dividir Nodo y asignar nueva raiz
                                self.raiz.claves.append(dato)
                                self.raiz.claves.sort()
                                nuevo=NodoArbolB()
                                nuevo.claves.append(self.raiz.claves[2])
                                nuevo.ramas[0]=self.raiz
                                otrapagina=NodoArbolB()
                                otrapagina.claves.append(self.raiz.claves[3])
                                otrapagina.claves.append(self.raiz.claves[4])
                                self.raiz.claves.pop()
                                self.raiz.claves.pop()
                                self.raiz.claves.pop()
                                nuevo.ramas[1]=otrapagina
                                self.raiz=nuevo
                            else:
                                self.raiz.claves.append(dato)
                                self.raiz.claves.sort()
        else:
            pagina.padre=padre
            if dato < pagina.claves[0]:
                if pagina.ramas[0]!=None:
                    self.InsertarB(pagina,pagina.ramas[0],dato)
                else:
                    self.Subir(pagina,dato)
            else:
                index=len(pagina.claves)
                while dato < pagina.claves[index-1] and index > 0:
                    index-=1
                if index > 0:
                    if pagina.ramas[index]!=None:
                        self.InsertarB(pagina,pagina.ramas[index],dato)
                    else:
                        self.Subir(pagina,dato)



    def CarpetaenUsuario(self,nombre,dato):
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.nombre==nombre:
                auxiliar.carpeta=self.raiz
                self.InsertarB(None,auxiliar.carpeta,dato)
                auxiliar.carpeta=self.raiz
            auxiliar=auxiliar.siguiente








Ar=ArbolB()
Ar.InsertarUsuario("mario",123)
Ar.InsertarUsuario("luna",456)
Ar.InsertarUsuario("Roberto",44)
Ar.CarpetaenUsuario("mario",4)
Ar.CarpetaenUsuario("mario",5)
Ar.CarpetaenUsuario("mario",6)
Ar.CarpetaenUsuario("mario",10)
Ar.CarpetaenUsuario("mario",12)
Ar.raiz=None
Ar.CarpetaenUsuario("luna",24)
Ar.CarpetaenUsuario("luna",21)
Ar.CarpetaenUsuario("luna",1)
Ar.raiz=None
Ar.CarpetaenUsuario("Roberto",100)

print(Ar.primero.carpeta.ramas[0].claves)

