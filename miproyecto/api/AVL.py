

class NodoArbol:

    def __init__(self,dato,bit):
        self.dato=dato
        self.bit=bit
        self.derecho=None
        self.izquierdo=None
        self.altura=0
        self.factor=0
        self.raiz=None
        self.padre=None



class Arbol:
    def __init__(self):
        self.concatenar="digraph g {\n"
        self.textoInOrden=""
        self.textobytes=""

    def InsertarAVL(self,arbol,dato,bit):
        if dato<arbol.dato:
            if arbol.izquierdo==None:
                arbol.izquierdo=NodoArbol(dato,bit)
            else:
                self.InsertarAVL(arbol.izquierdo,dato,bit)
        elif dato>arbol.dato:
            if arbol.derecho==None:
                arbol.derecho=NodoArbol(dato,bit)
            else:
                self.InsertarAVL(arbol.derecho,dato,bit)
        else:
            print("El dato: "+str(dato)+" ya esta repetido")


    def PreOrden(self,arbol):
        if arbol!=None:
            print(arbol.dato)
            self.PreOrden(arbol.izquierdo)
            self.PreOrden(arbol.derecho)


    def PosOrden(self,arbol):
        if arbol!=None:
            if arbol.izquierdo!=None:
                self.PosOrden(arbol.izquierdo)
            else:
                pass
            if arbol.derecho!=None:
                self.PosOrden(arbol.derecho)
            else:
                pass
            #print(arbol.dato)
            self.DarAltura(arbol)
            self.DarFactor(arbol)
            self.Equilibrar(arbol)
        else:
            print("el arbol esta vacio")

    def InOrden(self,arbol):
        if arbol!=None:
            self.InOrden(arbol.izquierdo)
            self.textoInOrden+=arbol.dato+","
            #print(arbol.dato)
            self.InOrden(arbol.derecho)
        return self.textoInOrden


    def InOrdenBits(self,arbol,archivo):
        if arbol!=None:
            #self.textobytes=""
            self.InOrdenBits(arbol.izquierdo,archivo)
            if archivo==arbol.dato:
                self.textobytes=str(arbol.bit)+","+str(arbol.dato)
            self.InOrdenBits(arbol.derecho,archivo)
        return self.textobytes






    def GraficarArbol(self,arbol):
        if arbol!=None:
            #print(arbol.dato)
            vector=arbol.dato.split(".")

            self.concatenar+= "nodo_" + str(vector[0]) + '[label="' +str(arbol.dato)+'"]\n'
            if arbol.izquierdo!=None:
                vector1=arbol.izquierdo.dato.split(".")
                self.concatenar+= "nodo_" + str(vector[0])+" -> " +"nodo_" + str(vector1[0])+ "\n"
                self.GraficarArbol(arbol.izquierdo)
            else:
                pass
            if arbol.derecho!=None:
                vector2=arbol.derecho.dato.split(".")
                self.concatenar+= "nodo_" + str(vector[0]) +" -> "+ "nodo_" + str(vector2[0])+ "\n"
                self.GraficarArbol(arbol.derecho)
            else:
                pass
        else:
            print("el arbol esta vacio")
        return self.concatenar

    def DarAltura(self,nodo):
        if nodo.izquierdo==None and nodo.derecho==None:
            nodo.altura=0
        else:
            if nodo.izquierdo==None and nodo.derecho!=None:
                nodo.altura=nodo.derecho.altura+1
            elif nodo.derecho==None and nodo.izquierdo!=None:
                nodo.altura=nodo.izquierdo.altura+1
            else:
                nodo.altura=self.maximo(nodo.izquierdo.altura,nodo.derecho.altura)+1

    def DarFactor(self,nodo):
        if nodo.izquierdo==None:
            if nodo.derecho==None:
                nodo.factor=0
            else:
                nodo.factor=(-1)-nodo.derecho.altura
        elif nodo.derecho==None:
            if nodo.izquierdo==None:
                nodo.factor=0
            else:
                nodo.factor=nodo.izquierdo.altura-(-1)
        else:
            nodo.factor=nodo.izquierdo.altura-nodo.derecho.altura


    def RotarIzqIzq(self,nodo):
        p=nodo
        n=nodo.izquierdo
        n1=nodo.izquierdo.izquierdo
        n.izquierdo=n1.derecho
        n1.derecho=n
        p.izquierdo=n1

    def RotarIzqIzq2(self,nodo):
        n=nodo
        n1=nodo.derecho
        n2=nodo.derecho.izquierdo
        n1.izquierdo=n2.derecho
        n2.derecho=n1
        n.derecho=n2

    def RotarDerDer(self,nodo):
        n=nodo
        n1=nodo.derecho
        n2=nodo.derecho.derecho
        n1.derecho=n2.izquierdo
        n2.izquierdo=n1
        n.derecho=n2
    def RotarDerDer2(self,nodo):
        n=nodo
        n1=nodo.izquierdo
        n2=nodo.izquierdo.derecho
        n1.derecho=n2.izquierdo
        n2.izquierdo=n1
        n.izquierdo=n2

    def RotarDerIzq(self,nodo):
        p=nodo
        n=nodo.derecho
        n1=nodo.derecho.derecho
        n2=nodo.derecho.derecho.izquierdo
        n1.izquierdo=n2.derecho
        n2.derecho=n1
        n.derecho=n2.izquierdo
        n2.izquierdo=n
        p.derecho=n2

    def RotarDerIzq2(self,nodo):
        p=nodo
        n=nodo.izquierdo
        n1=nodo.izquierdo.derecho
        n2=nodo.izquierdo.derecho.izquierdo
        n1.izquierdo=n2.derecho
        n2.derecho=n1
        n.derecho=n2.izquierdo
        n2.izquierdo=n
        p.izquierdo=n2

    def RotarIzqDer(self,nodo):
        p=nodo
        n=nodo.izquierdo
        n1=nodo.izquierdo.izquierdo
        n2=nodo.izquierdo.izquierdo.derecho
        n1.derecho=n2.izquierdo
        n2.izquierdo=n1
        n.izquierdo=n2.derecho
        n2.derecho=n
        p.izquierdo=n2

    def RotarIzqDer2(self,nodo):
        p=nodo
        n=nodo.derecho
        n1=nodo.derecho.izquierdo
        n2=nodo.derecho.izquierdo.derecho
        n1.derecho=n2.izquierdo
        n2.izquierdo=n1
        n.izquierdo=n2.derecho
        n2.derecho=n
        p.derecho=n2

    def Equilibrar(self,arbol):
        if arbol.izquierdo!=None:
            if arbol.izquierdo.factor==2:
                if arbol.izquierdo.izquierdo.factor==1:
                    self.RotarIzqIzq(arbol)
                elif arbol.izquierdo.izquierdo.factor==-1:
                    self.RotarIzqDer(arbol)
            elif arbol.izquierdo.factor==-2:
                if arbol.izquierdo.derecho.factor==-1:
                    self.RotarDerDer2(arbol)
                elif arbol.izquierdo.derecho.factor==1:
                    self.RotarDerIzq2(arbol)
        if arbol.derecho!=None:
            if arbol.derecho.factor==2:
                if arbol.derecho.izquierdo.factor==1:
                    self.RotarIzqIzq2(arbol)
                elif arbol.derecho.izquierdo.factor==-1:
                    self.RotarIzqDer2(arbol)
            elif arbol.derecho.factor==-2:
                if arbol.derecho.derecho.factor==-1:
                    self.RotarDerDer(arbol)
                elif arbol.derecho.derecho.factor==1:
                    self.RotarDerIzq(arbol)


    def EliminarAVL(self,nodo,dato):
        if nodo!=None:
            if dato < nodo.dato:
                if nodo.izquierdo!=None:
                    nodo.izquierdo.padre=nodo
                self.EliminarAVL(nodo.izquierdo,dato)

            elif dato > nodo.dato:
                if nodo.derecho!=None:
                    nodo.derecho.padre=nodo
                self.EliminarAVL(nodo.derecho,dato)
            else:
                if nodo.izquierdo==None:
                    nodo.padre.izquierdo=nodo.derecho
                elif nodo.derecho==None:
                    nodo.padre.derecho=nodo.izquierdo
                else:
                    nodo.padre.izquierdo=None




    def ModificarAVL(self,nodo,dato1,dato2):
        if nodo!=None:
            self.ModificarAVL(nodo.izquierdo,dato1,dato2)
            
            if dato1==nodo.dato:
                nodo.dato=dato2

            self.ModificarAVL(nodo.derecho,dato1,dato2)

                    



    def maximo(self,a,b):
        if a>b:
            return a
        elif b>a:
            return b
        else:
            return a
