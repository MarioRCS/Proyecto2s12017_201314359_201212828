

class NodoArbol:

    def __init__(self,dato):
        self.dato=dato
        self.derecho=None
        self.izquierdo=None
        self.altura=0
        self.factor=0
        self.raiz=None


class Arbol:
    def __init__(self):
        self.concatenar="digraph g {\n"

    def InsertarAVL(self,arbol,dato):
        if dato<arbol.dato:
            if arbol.izquierdo==None:
                arbol.izquierdo=NodoArbol(dato)
            else:
                self.InsertarAVL(arbol.izquierdo,dato)
        elif dato>arbol.dato:
            if arbol.derecho==None:
                arbol.derecho=NodoArbol(dato)
            else:
                self.InsertarAVL(arbol.derecho,dato)
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
            print(arbol.dato)
            self.InOrden(arbol.derecho)

    def GraficarArbol(self,arbol):
        if arbol!=None:
            #print(arbol.dato)
            self.concatenar+= "nodo_" + str(arbol.dato) +" [label=" +str(arbol.dato)+"]\n"
            if arbol.izquierdo!=None:
                self.concatenar+= "nodo_" + str(arbol.dato)+" -> " +"nodo_" + str(arbol.izquierdo.dato)+ "\n"
                self.GraficarArbol(arbol.izquierdo)
            else:
                pass
            if arbol.derecho!=None:
                self.concatenar+= "nodo_" + str(arbol.dato) +" -> "+ "nodo_" + str(arbol.derecho.dato)+ "\n"
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






    def maximo(self,a,b):
        if a>b:
            return a
        elif b>a:
            return b
        else:
            return a
