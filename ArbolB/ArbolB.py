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
        self.padre=None

class Carpeta():

    def __init__(self):
        self.nombre=""
        self.arbolb=None
        self.avl=None


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
        self.temp=None
        self.temp2=None

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
            carpeta=Carpeta()
            carpeta.nombre=dato
            padre.claves.append(carpeta)
            #padre.claves.sort()
            self.Ordenar(padre.claves)
            padre.ramas.append(None)
            index=len(padre.claves)
            while index > 1 and padre.claves[index-1].nombre > dato:
                padre.ramas[index]=padre.ramas[index-1]
                index-=1
            padre.ramas[index]=pagina2
            temp=padre.claves[2].nombre
            self.Subir(padre,temp)
            padre.ramas.pop()
            padre.ramas.pop()
            padre.ramas.pop()
        else:
            if dato < padre.claves[0]:
                carpeta=Carpeta()
                carpeta.nombre=dato
                padre.claves.append(carpeta)
                #padre.claves.sort()
                self.Ordenar(padre.claves)
                index=len(padre.claves)
                while index > 1:
                    padre.ramas[index]=padre.ramas[index-1]
                    index-=1
                padre.ramas[1]=pagina2
            else:
                carpeta=Carpeta()
                carpeta.nombre=dato
                padre.claves.append(carpeta)
                #padre.claves.sort()
                self.Ordenar(padre.claves)
                if pagina!=self.raiz:
                    padre.ramas.append(None)
                #aqui me quede
                index=len(padre.claves)
                while index > 0:
                    if padre.claves[index-1].nombre==dato:
                        padre.ramas[index]=pagina2
                    index-=1



    def Subir(self,pagina,dato):
        if len(pagina.claves)==4:
            carpeta=Carpeta()
            carpeta.nombre=dato
            pagina.claves.append(carpeta)
            #pagina.claves.sort()
            self.Ordenar(pagina.claves)
            temp=pagina.claves[2].nombre
            pagina2=NodoArbolB()
            carpeta1=Carpeta()
            carpeta1.nombre=pagina.claves[3].nombre
            carpeta2=Carpeta()
            carpeta.nombre=pagina.claves[4].nombre
            pagina2.claves.append(carpeta1)
            pagina2.claves.append(carpeta2)
            pagina.claves.pop()
            pagina.claves.pop()
            pagina.claves.pop()
            self.ReacomodarRamas(pagina,pagina.padre,pagina2,temp)
        elif len(pagina.claves)==5:
            temp=pagina.claves[2].nombre
            #print(temp)
            pagina2=NodoArbolB()
            carpeta=Carpeta()
            carpeta.nombre=pagina.claves[3].nombre
            carpeta1=Carpeta()
            carpeta1.nombre=pagina.claves[4].nombre
            pagina2.claves.append(carpeta)
            pagina2.claves.append(carpeta1)
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
                carpeta=Carpeta()
                carpeta.nombre=temp
                nuevo.claves.append(carpeta)
                nuevo.ramas[0]=pagina
                nuevo.ramas[1]=pagina2
                self.raiz=nuevo
            else:
                self.ReacomodarRamas(pagina,pagina.padre,pagina2,temp)
        else:
            carpeta=Carpeta()
            carpeta.nombre=dato
            pagina.claves.append(carpeta)
            #pagina.claves.sort()
            self.Ordenar(pagina.claves)

    def InsertarB(self,padre,pagina,dato):
        if pagina==self.raiz:
            #print("pasa")
            if pagina==None:
                self.raiz=NodoArbolB()
                carpeta=Carpeta()
                carpeta.nombre=dato
                self.raiz.claves.append(carpeta)
            else:
                if dato < self.raiz.claves[0].nombre:
                    if self.raiz.ramas[0]!=None:
                        self.InsertarB(self.raiz,self.raiz.ramas[0],dato)
                    else:
                        if self.estalleno(self.raiz):
                            #dividir Nodo y asignar nueva raiz
                            carpeta=Carpeta()
                            carpeta.nombre=dato
                            self.raiz.claves.append(carpeta)
                            #self.raiz.claves.sort()
                            self.Ordenar(self.raiz.claves)
                            nuevo=NodoArbolB()
                            carpeta1=Carpeta()
                            carpeta1.nombre=self.raiz.claves[2].nombre
                            nuevo.claves.append(carpeta1)
                            nuevo.ramas[0]=self.raiz
                            otrapagina=NodoArbolB()
                            carpeta2=Carpeta()
                            carpeta2.nombre=self.raiz.claves[3].nombre
                            carpeta3=Carpeta()
                            carpeta3.nombre=self.raiz.claves[4].nombre
                            otrapagina.claves.append(carpeta2)
                            otrapagina.claves.append(carpeta3)
                            self.raiz.claves.pop()
                            self.raiz.claves.pop()
                            self.raiz.claves.pop()
                            nuevo.ramas[1]=otrapagina
                            self.raiz=nuevo
                        else:
                            carpeta=Carpeta()
                            carpeta.nombre=dato
                            self.raiz.claves.append(carpeta)
                            #self.raiz.claves.sort()
                            self.Ordenar(self.raiz.claves)
                else:
                    index=len(self.raiz.claves)
                    while dato < self.raiz.claves[index-1].nombre and index > 0:
                        index-=1
                    if index > 0:
                        if self.raiz.ramas[index]!=None:
                            self.InsertarB(self.raiz,self.raiz.ramas[index],dato)
                        else:
                            if self.estalleno(self.raiz):
                                #dividir Nodo y asignar nueva raiz
                                carpeta=Carpeta()
                                carpeta.nombre=dato
                                self.raiz.claves.append(carpeta)
                                #self.raiz.claves.sort()
                                self.Ordenar(self.raiz.claves)
                                nuevo=NodoArbolB()
                                carpeta1=Carpeta()
                                carpeta1.nombre=self.raiz.claves[2].nombre
                                nuevo.claves.append(carpeta1)
                                nuevo.ramas[0]=self.raiz
                                otrapagina=NodoArbolB()
                                carpeta2=Carpeta()
                                carpeta2.nombre=self.raiz.claves[3].nombre
                                carpeta3=Carpeta()
                                carpeta3.nombre=self.raiz.claves[4].nombre
                                otrapagina.claves.append(carpeta2)
                                otrapagina.claves.append(carpeta3)
                                self.raiz.claves.pop()
                                self.raiz.claves.pop()
                                self.raiz.claves.pop()
                                nuevo.ramas[1]=otrapagina
                                self.raiz=nuevo
                            else:
                                carpeta=Carpeta()
                                carpeta.nombre=dato
                                self.raiz.claves.append(carpeta)
                                #self.raiz.claves.sort()
                                self.Ordenar(self.raiz.claves)
        else:
            #print("pasa2")
            pagina.padre=padre
            if dato < pagina.claves[0].nombre:
                if pagina.ramas[0]!=None:
                    self.InsertarB(pagina,pagina.ramas[0],dato)
                else:
                    self.Subir(pagina,dato)
            else:
                index=len(pagina.claves)
                while dato < pagina.claves[index-1].nombre and index > 0:
                    index-=1
                if index > 0:
                    if pagina.ramas[index]!=None:
                        self.InsertarB(pagina,pagina.ramas[index],dato)
                    else:
                        self.Subir(pagina,dato)

    def Ordenar(self,vector):
        temp=[]
        for elemento in vector:
            temp.append(elemento.nombre)
        temp.sort()
        index2=0
        for elemento2 in temp:
            vector[index2].nombre=temp[index2]
            index2+=1






    def CarpetaenUsuario(self,nombre,dato):
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.nombre==nombre:
                if auxiliar.carpeta==None:
                    auxiliar.carpeta=NodoArbolB()
                    carpeta=Carpeta()
                    carpeta.nombre=dato
                    auxiliar.carpeta.claves.append(carpeta)
                else:
                    self.raiz=auxiliar.carpeta
                    self.InsertarB(None,self.raiz,dato)
                    auxiliar.carpeta=self.raiz
            auxiliar=auxiliar.siguiente








    def buscar(self,raiz,dato):
        encontrado=False
        if dato<raiz.claves[0].nombre:
            if raiz.ramas[0]!=None:
                return self.buscar(raiz.ramas[0],dato)
            else:
                print("el dato no se encuentra en el arbol")
        else:
            index=len(raiz.claves)
            while index>0 and dato<=raiz.claves[index-1].nombre:
                if dato==raiz.claves[index-1].nombre:
                    #print("el dato: "+str(dato)+" fue encontrado")
                    return raiz
                    encontrado=True
                index-=1
            if encontrado==False:
                if index>0:
                    if raiz.ramas[index]!=None:
                        return self.buscar(raiz.ramas[index],dato)
                    else:
                        print("el dato no se encuentra en el arbol")
            else:
                pass







    def CrearenRuta(self,ruta,dato):
        if self.buscar(self.primero.carpeta,ruta).claves[self.IndicedelNodo(self.buscar(self.primero.carpeta,ruta).claves,ruta)].arbolb==None:
            self.buscar(self.primero.carpeta,ruta).claves[self.IndicedelNodo(self.buscar(self.primero.carpeta,ruta).claves,ruta)].arbolb=NodoArbolB()
            carpeta=Carpeta()
            carpeta.nombre=dato
            self.buscar(self.primero.carpeta,ruta).claves[self.IndicedelNodo(self.buscar(self.primero.carpeta,ruta).claves,ruta)].arbolb.claves.append(carpeta)
        else:
            self.raiz=self.buscar(self.primero.carpeta,ruta).claves[self.IndicedelNodo(self.buscar(self.primero.carpeta,ruta).claves,ruta)].arbolb
            self.InsertarB(None,self.raiz,dato)
            self.buscar(self.primero.carpeta,ruta).claves[self.IndicedelNodo(self.buscar(self.primero.carpeta,ruta).claves,ruta)].arbolb=self.raiz




    def EnRuta(self,ruta,dato):
        vector=ruta.split("/")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.carpeta==None:
                        auxiliar.carpeta=NodoArbolB()
                        carpeta=Carpeta()
                        carpeta.nombre=dato
                        auxiliar.carpeta.claves.append(carpeta)
                    else:
                        self.raiz=auxiliar.carpeta
                        self.InsertarB(None,self.raiz,dato)
                        auxiliar.carpeta=self.raiz
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,int(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,int(vector[indicador])).claves,int(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,int(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,int(vector[indicador])).claves,int(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.arbolb==None:
                        self.temp.arbolb=NodoArbolB()
                        carpeta=Carpeta()
                        carpeta.nombre=dato
                        self.temp.arbolb.claves.append(carpeta)
                    else:
                        self.raiz=self.temp.arbolb
                        self.InsertarB(None,self.raiz,dato)
                        self.temp.arbolb=self.raiz
            auxiliar=auxiliar.siguiente




    def IndicedelNodo(self,vector,dato):
        temp=[]
        for elemento in vector:
            temp.append(elemento.nombre)
        indice=temp.index(dato)
        return indice

Ar=ArbolB()



Ar.InsertarUsuario("mario",123)
Ar.InsertarUsuario("roberto",456)
Ar.InsertarUsuario("toro",789)


Ar.CarpetaenUsuario("roberto",15)
Ar.CarpetaenUsuario("roberto",16)
Ar.CarpetaenUsuario("mario",12)
Ar.CarpetaenUsuario("roberto",17)
Ar.CarpetaenUsuario("roberto",18)
Ar.CarpetaenUsuario("roberto",6)
Ar.CarpetaenUsuario("mario",25)

Ar.CrearenRuta(25,10)
Ar.CrearenRuta(25,8)
Ar.CrearenRuta(25,14)
Ar.CrearenRuta(12,2)
Ar.CrearenRuta(25,45)
Ar.CrearenRuta(25,11)

#print(Ar.primero.carpeta.claves[0].arbolb.claves[0].nombre)
#print(Ar.buscar(Ar.primero.carpeta,25))
#print(Ar.primero.carpeta)
Ar.EnRuta("mario/root/25/10",78)
print(Ar.primero.carpeta.claves[1].arbolb.ramas[0].claves[1].arbolb.claves[0].nombre)