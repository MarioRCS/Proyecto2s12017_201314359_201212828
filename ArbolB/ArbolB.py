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



class ArbolB():
    def __init__(self):
        self.raiz=None
    def size(self,claves):
        index=0
        while numero[index]!=None:
            index+=1
        return index





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
                #print("hola1")
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








Ar=ArbolB()

Ar.InsertarB(None,Ar.raiz,20)
Ar.InsertarB(None,Ar.raiz,40)
Ar.InsertarB(None,Ar.raiz,10)
Ar.InsertarB(None,Ar.raiz,30)
Ar.InsertarB(None,Ar.raiz,15)
Ar.InsertarB(None,Ar.raiz,35)
Ar.InsertarB(None,Ar.raiz,7)
Ar.InsertarB(None,Ar.raiz,26)
Ar.InsertarB(None,Ar.raiz,18)
Ar.InsertarB(None,Ar.raiz,22)
Ar.InsertarB(None,Ar.raiz,5)
Ar.InsertarB(None,Ar.raiz,42)
Ar.InsertarB(None,Ar.raiz,13)
Ar.InsertarB(None,Ar.raiz,46)
Ar.InsertarB(None,Ar.raiz,27)
Ar.InsertarB(None,Ar.raiz,8)
Ar.InsertarB(None,Ar.raiz,32)
Ar.InsertarB(None,Ar.raiz,38)
Ar.InsertarB(None,Ar.raiz,24)
Ar.InsertarB(None,Ar.raiz,45)
Ar.InsertarB(None,Ar.raiz,25)
Ar.InsertarB(None,Ar.raiz,48)
Ar.InsertarB(None,Ar.raiz,50)
Ar.InsertarB(None,Ar.raiz,0)
Ar.InsertarB(None,Ar.raiz,2)
Ar.InsertarB(None,Ar.raiz,16)
#Ar.InsertarB(None,Ar.raiz,12)
print(Ar.raiz.ramas[0].ramas[3].claves)

