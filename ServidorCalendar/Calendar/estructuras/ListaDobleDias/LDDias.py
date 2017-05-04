from graphviz import Source
from .NodoLDD import NodoLDD

class ListaDobleDias(object):
	
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.indice = 0
		self.grafo = ""
		
	def estaVacia(self):
		if self.inicio == None:
			return True
		else:
			return False

	def insertarInicio(self, dia):
		nuevo = NodoLDD(self.indice, dia)
		
		if self.estaVacia() == True:
			self.inicio = self.fin = nuevo
		else:
			nuevo.siguiente = self.inicio
			self.inicio.anterior = nuevo
			self.inicio = nuevo

		self.indice += 1

	def insertarFinal(self, dia):
		nuevo = NodoLDD(self.indice, dia)

		if self.estaVacia() == True:
			self.fin = self.inicio = nuevo
		else:
			nuevo.anterior = self.fin
			self.fin.siguiente = nuevo
			self.fin = nuevo

		self.indice += 1

	def insetarOrdenado(self, dia):
		nuevo = NodoLDD(self.indice, dia)
		temp = self.inicio

		if self.estaVacia() == True:
			self.inicio = nuevo
			self.inicio.siguiente = None
			self.inicio.anterior = None
			self.fin = self.inicio
			return

		while temp != None:
			if dia < temp.getDia():
				break
			temp = temp.siguiente
		
		if temp == None:
			self.fin.siguiente = nuevo
			nuevo.anterior = self.fin
			self.fin = nuevo
		elif temp == self.inicio:
			nuevo.siguiente = self.inicio
			self.inicio.anterior = nuevo
			self.inicio = nuevo
		else:
			temp.anterior.siguiente = nuevo
			nuevo.anterior = temp.anterior
			nuevo.siguiente = temp
			temp.anterior = nuevo

	def buscar(self, dia):
		temp = self.inicio
		encontrado = False

		while temp != None and encontrado != True:
			if temp.getDia() == dia:
				encontrado = True
				print("Dia: " + str(temp.getDia()) + " encontrado en el indice " + str(temp.getIndice()))
				return temp
			else:
				temp = temp.siguiente
		return None

	def mostrarInicioFin(self):
		if self.estaVacia() == True:
			print ("Lista Vacia")
		else:
			temp = self.inicio
			while temp != None:
				print (temp.getIndice() , "--" , temp.getDia())
				temp = temp.siguiente

	def mostrarFinInicio(self):
		if self.estaVacia() == True:
			print ("Lista Vacia")
		else:
			temp = self.fin
			while temp != None:
				print (temp.getIndice() , "--" , temp.getDia())
				temp = temp.anterior			

	def eliminar(self, dia):
		if self.inicio != None:
			temp = self.inicio
			temp2 = None
			while temp != self.fin:
				if temp.getDia() == dia:
					if temp2 == None:
						self.inicio = self.inicio.siguiente
						self.inicio.anterior = None
						temp.siguiente = None
						temp = self.inicio
					else:
						temp2.siguiente = temp.siguiente
						temp2.siguiente.anterior = temp.anterior
						temp.siguiente = None
						temp = temp2.siguiente
				else:
					temp2 = temp
					temp = temp.siguiente

			if dia == temp.getDia():
				self.fin = temp.anterior
				self.fin.siguiente = None

	def graficar(self):
		self.grafo = "digraph G {\n" + "graph [rankdir = TB];\n" + "node [shape = record,height=.1];  {\n"

		if self.estaVacia() == True:
			self.grafo += "\"ListaVacia\" [label = \"Lista Vacia\"]"
		else:
			temp = self.inicio
			i = 0
			while temp != None:
				self.grafo += "\"" + str(i) + "\" [label = \"" + str(temp.getDia()) + "\"];\n"
				if i > 0:
					self.grafo +=  "\"" + str(i - 1) + "\" -> \"" + str(i) + "\" ;\n"
					self.grafo +=  "\"" + str(i) + "\" -> \"" + str(i - 1) + "\" ;\n"

				temp = temp.siguiente
				i = i + 1

		self.grafo += "} labelloc=\"t\"; label=\" LISTA DOBLE DIAS\";}"
		print(self.grafo)
		src = Source(self.grafo)
		src.format = "png"
		src.render('test-output/ListaDobleUsuarios', view = True)
#**************************************************************************#
#************************* METODOS PARA LA MATRIZ *************************#
	#******************** INSERCIÓN ********************#
	def insertarHashLD(self, dia, evento, desc, direc, hora):
		diaEvento = self.buscar(dia)
		print(diaEvento.getIndice())
		if dia == diaEvento.getDia():			
			diaEvento.insertarHash(evento, desc, direc, hora)
			print("Nodo insertado en Lista: " + str(diaEvento.getDia()) + "--" + evento)

	def modificarHashLD(self, dia, name, desc, direc, hora):
		diaEvento = self.buscar(dia)
		if dia == diaEvento.getDia():
			diaEvento.modificarHash(name, desc, direc, hora)
			print("Evento Modificado")

	def graficarHashLD(self, dia):
		diaEvento = self.buscar(dia)
		print(str(diaEvento.getDia()))
		if dia == diaEvento.getDia():
			diaEvento.graficarHash()
