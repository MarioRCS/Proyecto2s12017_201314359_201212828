from graphviz import Source
from .ListaIndice import ListaIndice
from .NodoIndice import NodoIndice
from .NodoListaNodos import NodoListaNodos

class Matriz(object):
	def __init__(self):
		self.ejeX = ListaIndice()
		self.ejeY = ListaIndice()
		self.indice = ""
		self.diaEvento = NodoListaNodos("")
		#self.xml = ""

	def getNodoIndiceX(self, posX):
		nodoIndiceX = self.ejeX.buscar(posX)
		if nodoIndiceX == None:
			nodoIndiceX = NodoIndice(posX)
			self.ejeX.insertarIndice(nodoIndiceX)
		return nodoIndiceX

	def getNodoIndiceY(self, posY):
		nodoIndiceY = self.ejeY.buscar(posY)
		if nodoIndiceY == None:
			nodoIndiceY = NodoIndice(posY)
			self.ejeY.insertarIndice(nodoIndiceY)
		return nodoIndiceY
#**************************************************************************#
#************************* METODOS PARA LA MATRIZ *************************#
	#******************** INSERCIÓN ********************#
	def insertar(self, dia, mes, anio, evento, desc, direc, hora):
		posX = anio
		posY = mes
		
		nodoIndiceX = self.getNodoIndiceX(posX)
		nodoIndiceY = self.getNodoIndiceY(posY)
		nodo = self.buscar(posX, posY)
		if evento != None:
			if nodo == None:
				nodo = NodoListaNodos(str(dia))
				nodo.padreX = nodoIndiceX
				nodo.padreY = nodoIndiceY
				nodoIndiceX.listaNodos.insertarX(nodo)
				nodoIndiceY.listaNodos.insertarY(nodo)
				nodo.insertarLD(dia)
				nodo.insertarHashMatriz(dia, evento, desc, direc, hora)
			else:
				print("df")
				if nodo.buscarLD(dia) == None:
					nodo.insertarLD(dia)
					nodo.insertarHashMatriz(dia, evento, desc, direc, hora)
					print("creando nuevo dia")
				else:
					nodo.insertarHashMatriz(dia, evento, desc, direc, hora)
					print ("insertando evento")
				#nodo.agregarDia(str(dia))
	#******************** BÚSQUEDA ********************#
	def buscar(self, anio, mes):
		tempY = self.ejeY.inicio
		while tempY != None:
			tempXinterno = tempY.listaNodos.inicio
			if tempY.getIndice() == mes:
				while tempXinterno != None:
					if tempXinterno.padreX.getIndice() == anio:
						self.diaEvento = tempXinterno
						print("Nodo " + str(self.diaEvento.getDia()) + " encontrado")
						return tempXinterno
					#else:
					#	print("Empresa incorrecta o no existe")
					tempXinterno = tempXinterno.derecha
			#else:
				#print("Departamento incorrecto o no existe")			
			tempY = tempY.siguiente
		return None
	#****************** ELIMINACIÓN *******************#
	def eliminar(self, dia, mes, anio):
		tempY = self.ejeY.inicio
		while tempY != None:
			if self.ejeY.inicio != None:
				tempY = self.ejeY.inicio
				temp2 = None
				while tempY != self.ejeY.fin:
					if tempY.getIndice() == mes:
						if temp2 == None:
							self.ejeY.inicio = self.ejeY.inicio.abajo
							self.ejeY.inicio.arriba = None
							tempY.abajo = None
							tempY = self.ejeX.inicio
						else:
							temp2.abajo = tempY.abajo
							temp2.abajo.arriba = tempY.arriba
							tempY.abajo = None
							tempY = temp2.abajo
					else:
						temp2 = tempY
						tempY = tempY.abajo
				if mes == tempY.getIndice():
					self.ejeY.fin = tempY.arriba
					self.ejeY.fin.abajo = None
	#******************** GRAFICAR ********************#
	def graficar(self):
		grafo = "digraph G {\n" + "rankdir = TB;\n" + "rank = min;\n" + "node[style=filled,shape=box, label=\"Inicio\", rankdir=UD];\n"

		tempX = self.ejeX.inicio
		tempXinterno = None
		tempY = self.ejeY.inicio

		j = 0;
		i = 0;

		while tempY != None:
			if tempY == self.ejeY.inicio:
				grafo += "\"" + str(i) + "," + str(j) + "\"[label=\"raiz\", style=filled];\n"
				i += 1
				while tempX != None:
					grafo += "\"" + str(i) + "," + str(j) + "\"[label=\""+tempX.getIndice()+"\", style=filled];\n"
					i += 1
					tempX = tempX.siguiente
				i = 0
				j += 1
			tempXinterno = tempY.listaNodos.inicio
			tempX = self.ejeX.inicio
			grafo += "\"" + str(i) + "," + str(j) + "\"[label=\""+tempY.getIndice()+"\", style=filled];\n"
			i += 1
			while tempX != None:
				if tempXinterno != None:
					if tempXinterno.padreX == tempX:
						grafo += "\"" + str(i) + "," + str(j) + "\"[label=\"Dia: "+ str(tempXinterno.getDia()) + "\", style=filled];\n"
						tempXinterno = tempXinterno.derecha
					else:
						grafo += "\"" + str(i) + "," + str(j) + "\"[label=\"no existe\", style=filled];\n"
				else:
					grafo += "\"" + str(i) + "," + str(j) + "\"[label=\"no existe\", style=filled];\n"
				i += 1
				tempX = tempX.siguiente
			i = 0
			j += 1
			tempY = tempY.siguiente
		print(str(i))
		print(str(j))
		tempX = self.ejeX.inicio
		while tempX != None:
			i += 1
			tempX = tempX.siguiente
		print(str(i))
		print(str(j))
		i += 1
		for y in range(0,j):
		    for x in range (0,i-1):
		        grafo += "\"" + str(x) + "," + str(y) + "\" -> \"" + str(x + 1) + "," + str(y) + "\"[constraint=false];\n"
		        grafo += "\"" + str(x + 1) + "," + str(y) + "\" -> \"" + str(x) + "," + str(y) + "\"[constraint=false];\n"
		        grafo += "{rank=same;\"" + str(x) + "," + str(y) + "\" \"" + str(x + 1) + "," + str(y) + "\"}\n"
		        grafo += "{rank=same;\"" + str(x + 1) + "," + str(y) + "\" \"" + str(x) + "," + str(y) + "\"}\n"

		for y in range(0,j-1):
		    for x in range (0,i):
		        grafo += "\"" + str(x) + "," + str(y) + "\" -> \"" + str(x) + "," + str(y + 1) + "\"[rankdir=UD];\n";
		        grafo += "\"" + str(x) + "," + str(y + 1) + "\" -> \"" + str(x) + "," + str(y) + "\"[rankdir=UD];\n";

		grafo += "labelloc=\"t\"; label=\" MATRIZ DISPERSA CALENDARIO\";}"
		print(grafo)
		
		src = Source(grafo)
		src.format = "png"
		src.render('test-output/MatrizDispersa', view = True)
		#return grafo
#**************************************************************************#
#*************************** METODOS PARA LA LD ***************************#
	#********************** GRAFICAR **********************#
	def graficarLDMatriz(self, anio, mes):
		self.buscar(anio, mes)
		#print(self.diaEvento.getDia())
		#if dia == self.diaEvento.getDia():
			#print("entro al if")
		graf = self.diaEvento.graficarLD()
		print(graf)
#*************************** METODOS PARA HASH ***************************#
	#********************** MODIFICAR **********************#
	def modificarHashMatriz(self, anio, mes, dia, name, desc, direc, hora):
		self.buscar(anio, mes)
		evento = self.diaEvento.buscarLD(dia)
		if dia == evento.getDia():
			self.diaEvento.modificarHashMatriz(dia, name, desc, direc, hora)
	#********************** ELIMINAR **********************#
	def eliminarHashMatriz(self, anio, mes, dia, name):
		self.buscar(anio, mes)
		evento = self.diaEvento.buscarLD(dia)
		if dia == evento.getDia():
			self.diaEvento.eliminarHashMatriz(dia, name)
	#********************** GRAFICAR **********************#
	def graficarHashMatriz(self, anio, mes, dia):
		self.buscar(anio, mes)
		#print(self.diaEvento.getDia())
		evento = self.diaEvento.buscarLD(dia)
		#print(evento.getDia())
		if dia == evento.getDia():
			print("entro al if")
			graf = self.diaEvento.graficarHashMatriz(dia)
			print(graf)
#**************************************************************************#