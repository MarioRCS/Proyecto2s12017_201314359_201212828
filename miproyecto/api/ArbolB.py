# -*- coding: utf-8 -*-

from AVL import Arbol,NodoArbol

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
        self.archivo=None

class NodoBitacora():
    def __init__(self):
        self.siguiente=None
        self.nombre=""
        self.id=0




class ArbolB():
    def __init__(self):
        self.raiz=None
        self.primero=None
        self.primeroB=None
        self.ultimo=None
        self.temp=None
        self.temp2=None
        self.concatenar=""
        self.textoB="digraph g{\n"+'rankdir = "'+"UD"+'"\n'
        self.textoBenRuta=""
        self.textoCarpeta=""
        self.textoCarpetaRuta=""
        self.textoAvl=""
        self.textoarchivo=""
        self.textoBits=""
        self.num=0
        self.textoBitacora="digraph g{\n"


    def InsertarBitacora(self,dato,iden):
        if self.primeroB==None:
            nuevo=NodoBitacora()
            nuevo.nombre=dato
            nuevo.id=iden
            self.primeroB=nuevo
        else:
            auxiliar=self.primeroB
            while auxiliar.siguiente!=None:
                auxiliar=auxiliar.siguiente

            auxiliar.siguiente=NodoBitacora()
            auxiliar.nombre=dato
            auxiliar.id=iden

    def GraficarBitacora(self):
        auxiliar=self.primeroB
        while auxiliar!=None:
            self.textoBitacora+="nodo"+str(auxiliar.id)+'[label="'+auxiliar.nombre+'"];\n'
            auxiliar=auxiliar.siguiente

        auxiliar2=self.primeroB
        while auxiliar2.siguiente!=None:
            self.textoBitacora+="nodo"+str(auxiliar2.id)+" -> "+"nodo"+str(auxiliar2.siguiente.id)+";\n"
            auxiliar2=auxiliar2.siguiente

        return self.textoBitacora






    def size(self,claves):
        index=0
        while numero[index]!=None:
            index+=1
        return index

    def InsertarUsuario(self,nombre,contrasenia):
        if self.primero==None:
            nuevo=NodoLista()
            nuevo.siguiente=None
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




    def CarpetaEnRuta(self,ruta,dato):
        vector=ruta.split('A')
        auxiliar=self.primero
        while auxiliar!=None:
            if str(vector[0])==auxiliar.nombre:
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
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
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



    def ArchivoEnRuta(self,ruta,dato,bit):
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.archivo==None:
                        auxiliar.archivo=NodoArbol(dato,bit)
                    else:
                        ar=Arbol()
                        ar.InsertarAVL(auxiliar.archivo,dato,bit)
                        ar.PosOrden(auxiliar.archivo)
                        if auxiliar.archivo.factor==2:
                            if auxiliar.archivo.izquierdo.factor==1:
                                n=auxiliar
                                n1=auxiliar.archivo
                                n2=auxiliar.archivo.izquierdo
                                n1.izquierdo=n2.derecho
                                n2.derecho=n1
                                n.archivo=n2
                            elif auxiliar.archivo.izquierdo.factor==-1:
                                p=auxiliar
                                n=auxiliar.archivo
                                n1=auxiliar.archivo.izquierdo
                                n2=auxiliar.archivo.izquierdo.derecho
                                n1.derecho=n2.izquierdo
                                n2.izquierdo=n1
                                n.izquierdo=n2.derecho
                                n2.derecho=n
                                p.archivo=n2
                        elif auxiliar.archivo.factor==-2:
                            if auxiliar.archivo.derecho.factor==-1:
                                p=auxiliar
                                n=auxiliar.archivo
                                n1=auxiliar.archivo.derecho
                                n.derecho=n1.izquierdo
                                n1.izquierdo=n
                                p.archivo=n1
                            elif auxiliar.archivo.derecho.factor==1:
                                p=auxiliar
                                n=auxiliar.archivo
                                n1=auxiliar.archivo.derecho
                                n2=auxiliar.archivo.derecho.izquierdo
                                n1.izquierdo=n2.derecho
                                n2.derecho=n1
                                n.derecho=n2.izquierdo
                                n2.izquierdo=n
                                p.archivo=n2
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.avl==None:
                        self.temp.avl=NodoArbol(dato,bit)
                    else:
                        ar=Arbol()
                        ar.InsertarAVL(self.temp.avl,dato,bit)
                        ar.PosOrden(self.temp.avl)
                        if self.temp.avl.factor==2:
                            if self.temp.avl.izquierdo.factor==1:
                                n=self.temp
                                n1=self.temp.avl
                                n2=self.temp.avl.izquierdo
                                n1.izquierdo=n2.derecho
                                n2.derecho=n1
                                n.avl=n2
                            elif self.temp.avl.izquierdo.factor==-1:
                                p=self.temp
                                n=self.temp.avl
                                n1=self.temp.avl.izquierdo
                                n2=self.temp.avl.izquierdo.derecho
                                n1.derecho=n2.izquierdo
                                n2.izquierdo=n1
                                n.izquierdo=n2.derecho
                                n2.derecho=n
                                p.avl=n2
                        elif self.temp.avl.factor==-2:
                            if self.temp.avl.derecho.factor==-1:
                                p=self.temp
                                n=self.temp.avl
                                n1=self.temp.avl.derecho
                                n.derecho=n1.izquierdo
                                n1.izquierdo=n
                                p.avl=n1
                            elif self.temp.avl.derecho.factor==1:
                                p=self.temp
                                n=self.temp.avl
                                n1=self.temp.avl.derecho
                                n2=self.temp.avl.derecho.izquierdo
                                n1.izquierdo=n2.derecho
                                n2.derecho=n1
                                n.derecho=n2.izquierdo
                                n2.izquierdo=n
                                p.avl=n2

            auxiliar=auxiliar.siguiente


    def AvlEnRuta(self,ruta):
        self.textoAvl=""
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.archivo==None:
                        print("No se puede Graficar en esta ruta")
                    else:
                        avl=Arbol()
                        self.textoAvl=avl.GraficarArbol(auxiliar.archivo)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.avl==None:
                        print("no se puede Graficar en esta ruta")
                    else:
                        avl=Arbol()
                        self.textoAvl=avl.GraficarArbol(self.temp.avl)
            auxiliar=auxiliar.siguiente

        return self.textoAvl




    def ActualizarArchivos(self,ruta):
        self.textoarchivo=""
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.archivo==None:
                        print("No se puede Graficar en esta ruta")
                    else:
                        avl=Arbol()
                        self.textoarchivo=avl.InOrden(auxiliar.archivo)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.avl==None:
                        print("no se puede Graficar en esta ruta")
                    else:
                        avl=Arbol()
                        self.textoarchivo=avl.InOrden(self.temp.avl)
            auxiliar=auxiliar.siguiente

        return self.textoarchivo





    def EliminarAvlRuta(self,ruta,dato):
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.archivo==None:
                        print("No se puede Eliminar en esta ruta")
                    else:
                        avl=Arbol()
                        avl.EliminarAVL(auxiliar.archivo,dato)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.avl==None:
                        print("no se puede Eliminar en esta ruta")
                    else:
                        avl=Arbol()
                        avl.EliminarAVL(self.temp.avl,dato)
            auxiliar=auxiliar.siguiente


    def ModificaCarpeta(self,nodo,nombre1,nombre2):
        if nodo!=None:
            for elemento in nodo.claves:    
                if nombre1==elemento.nombre:
                    elemento.nombre=nombre2            
            index=len(nodo.claves)
            item=0
            while item<=index:
                if nodo.ramas[item]!=None:
                    self.ModificaCarpeta(nodo.ramas[item],nombre1,nombre2)
                item+=1
                
        else:
            print("no se puede borrar porque no hay arbolb")



    def ModificarBenRuta(self,ruta,nombre1,nombre2):
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.carpeta==None:
                        print("no existe carpeta para  Modificar")
                    else:
                        self.ModificaCarpeta(auxiliar.carpeta,nombre1,nombre2)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.arbolb==None:
                        print("no existe carpeta para Modificar")
                    else:
                        self.ModificaCarpeta(self.temp.arbolb,nombre1,nombre2)
            auxiliar=auxiliar.siguiente
        





    def GetBits(self,ruta,archivo):
        self.textoBits=""
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.archivo==None:
                        print("No se puede Graficar en esta ruta")
                    else:
                        avl=Arbol()
                        self.textoBits=avl.InOrdenBits(auxiliar.archivo,archivo)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.avl==None:
                        print("no se puede Graficar en esta ruta")
                    else:
                        avl=Arbol()
                        self.textoBits=avl.InOrdenBits(self.temp.avl,archivo)
            auxiliar=auxiliar.siguiente
        return self.textoBits




    def ModificarArchivoRuta(self,ruta,dato1,dato2):
        self.textoBits=""
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.archivo==None:
                        print("No se puede Modificar el archivo en esta ruta")
                    else:
                        avl=Arbol()
                        avl.ModificarAVL(auxiliar.archivo,dato1,dato2)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.avl==None:
                        print("no se puede Modificar Archivo en esta ruta")
                    else:
                        avl=Arbol()
                        avl.ModificarAVL(self.temp.avl,dato1,dato2)
            auxiliar=auxiliar.siguiente
        





    def EliminarB(self, nodo,carpeta):
        if nodo!=None:
            for elemento in nodo.claves:    
                if carpeta==elemento.nombre:
                    nodo.claves.remove(nodo.claves[self.IndicedelNodo(nodo.claves,carpeta)])
            
            index=len(nodo.claves)
            item=0
            while item<=index:
                if nodo.ramas[item]!=None:
                    self.EliminarB(nodo.ramas[item],carpeta)
                item+=1
                
        else:
            print("no se puede borrar porque no hay arbolb")



    def EliminarBenRuta(self,ruta,carpeta):
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.carpeta==None:
                        print("no existe carpeta para  Eliminar")
                    else:
                        self.EliminarB(auxiliar.carpeta,carpeta)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.arbolb==None:
                        print("no existe carpeta para Eliminar")
                    else:
                        self.EliminarB(self.temp.arbolb,carpeta)
            auxiliar=auxiliar.siguiente
        







    def GraficarBenRuta(self,ruta):
        self.textoBenRuta=""
        vector=ruta.split("A")
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.carpeta==None:
                        print("no se puede Graficar en esta Ruta")
                    else:
                        self.textoBenRuta=self.GraficarArbolB(auxiliar.carpeta)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.arbolb==None:
                        print("no se puede Graficar en esta Ruta")
                    else:
                        self.textoBenRuta=self.GraficarArbolB(self.temp.arbolb)
            auxiliar=auxiliar.siguiente
        return self.textoBenRuta





    def Login(self,nombre,contrasenia):
        acceso=False
        auxiliar=self.primero
        while auxiliar!=None:
            if auxiliar.nombre==nombre and auxiliar.contrasenia==contrasenia:
                acceso=True
            auxiliar=auxiliar.siguiente
        return acceso


    def GraficarLista(self):
        self.concatenar=""
        self.concatenar+="digraph g { \n"
        self.concatenar+="rankdir=LR;\n"
        auxiliar=self.primero
        while auxiliar!=None:
            self.concatenar+="n_"+auxiliar.nombre+'[label="'+str(auxiliar.nombre)+"\n"+str(auxiliar.contrasenia)+'"]; \n'
            auxiliar=auxiliar.siguiente

        auxiliar2=self.primero
        while auxiliar2.siguiente!=None:
            self.concatenar+="n_"+auxiliar2.nombre+" -> "+"n_"+auxiliar2.siguiente.nombre+";\n"
            auxiliar2=auxiliar2.siguiente
            self.concatenar+="n_"+auxiliar2.nombre+" -> "+"n_"+auxiliar2.anterior.nombre+";\n"
        self.concatenar+="}\n"

        return self.concatenar



    def IndicedelNodo(self,vector,dato):
        temp=[]
        for elemento in vector:
            temp.append(elemento.nombre)
        indice=temp.index(dato)
        return indice


    def GraficarArbolB(self, nodo):
        if nodo!=None:
            texto=""
            for elemento in nodo.claves:
                texto+=str(elemento.nombre)
            self.textoB+="nodo"+texto+"[label=\""
            for elemento in nodo.claves:
                self.textoB+=str(elemento.nombre)
                if nodo.claves.index(elemento)<len(nodo.claves)-1:
                    self.textoB+="|"

            self.textoB+="\"\n"
            self.textoB+='shape="'+"record"+'"\n'
            self.textoB+="];\n"
        index=len(nodo.claves)
        item=0
        while item<=index:
            if nodo.ramas[item]!=None:
                texto2=""
                for elemento in nodo.claves:
                    texto2+=str(elemento.nombre)
                texto3=""
                for elemento in nodo.ramas[item].claves:
                    texto3+=str(elemento.nombre)
                self.textoB+="nodo"+texto2+" -> "+"nodo"+texto3+"\n"

                self.GraficarArbolB(nodo.ramas[item])
            item+=1

        return self.textoB



    def ActualizarCarpetas(self,nodo):
        if nodo!=None:
            texto2=""
            texto=""
            for elemento in nodo.claves:
                texto+=str(elemento.nombre)+","
            texto2+=texto
            index=len(nodo.claves)
            item=0
            while item<=index:
                if nodo.ramas[item]!=None:
                    texto2+=self.ActualizarCarpetas(nodo.ramas[item])
                item+=1
            self.textoCarpeta=texto2
        return self.textoCarpeta


    def ActualizarCarpetaenRuta(self,ruta):
        self.textoCarpetaRuta=""
        print(ruta)
        vector=ruta.split('A')
        auxiliar=self.primero
        while auxiliar!=None:
            if vector[0]==auxiliar.nombre:
                #print("hola")
                index=len(vector)
                if index==2:
                    if auxiliar.carpeta==None:
                        print("no existen Carpetas en la ruta")
                    else:
                        self.textoCarpetaRuta=self.ActualizarCarpetas(auxiliar.carpeta)
                else:
                    indicador=2
                    while indicador < index:
                        if indicador==2:
                            self.temp=self.buscar(auxiliar.carpeta,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(auxiliar.carpeta,str(vector[indicador])).claves,str(vector[indicador]))]
                            indicador+=1
                        else:
                            self.temp2=self.temp
                            print(self.temp2.nombre)
                            self.temp=self.buscar(self.temp2.arbolb,str(vector[indicador])).claves[self.IndicedelNodo(self.buscar(self.temp2.arbolb,str(vector[indicador])).claves,str(vector[indicador]))]
                            print(self.temp.nombre)
                            indicador+=1
                    if self.temp.arbolb==None:
                        print("no se existen Carpetas en esta Ruta")
                    else:
                        self.textoCarpetaRuta=self.ActualizarCarpetas(self.temp.arbolb)
            auxiliar=auxiliar.siguiente
        return self.textoCarpetaRuta

    def ArchivoMultimedia(self,path,path2):
        f =open(path,'rb')
        temp=f.read()
        f.close()
        fo=open(path2,'wb')
        fo.write(temp)
        fo.close()

