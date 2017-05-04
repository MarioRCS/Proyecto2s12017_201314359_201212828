from graphviz import Source
from .NodoTH import NodoTH

class TablaHash(object):

	def __init__ (self):
		self.factorCarga = 0
		self.elementos = 0
		self.clave = 0
		self.posicion = 0
		self.size = 300
		self.table = []
		self.nodo = "","","","","",""
		
		for i in range(self.size):
			self.table.append(None)

	def obtenerASCII(self, nombre):
		self.clave = 0
		for caracter in nombre:
			self.clave += ord(caracter)
		#print(str(self.clave) + "--" + nombre)
		return self.clave

	def obtenerPosicion(self, nombre):
		d = self.obtenerASCII(nombre)
		#print (d)
		#******** funcion hash ********#
		p = d ** 2
		i = 0
		str_p = str(p)
		if len(str_p) >= 6:
			subP = str_p[len(str_p)-6:len(str_p)-3]
		else:
			subP = str_p[:len(str_p)-3]
		intP = int(subP)

		if intP > self.size:
			self.posicion = intP - self.size
			print(self.posicion)
		else:
			self.posicion = intP

		#print(str(self.posicion))
		#self.posicion = p
		#******** colisiones ********#
		while ((self.table[self.posicion] != None) and (not(self.table[self.posicion].getNombre() == nombre))):
			i += 1
			#print("Ocurrio una colision en: " + str(self.posicion))
			self.posicion = self.posicion + i
			#self.posicion = self.posicion ** 2
		#print(str(d) + "--" + nombre + "--" + str(self.posicion))
		return self.posicion

	def insertar(self, nombre, desc, direc, hora, nodo):
		self.posicion = self.obtenerPosicion(nombre)
		nodo = NodoTH(self.clave, nombre, desc, direc, hora, self.posicion)
		#print(str(self.posicion))
		self.table[self.posicion] = nodo
		#print (str(nodo.getPosicion()))
		self.elementos += 1
		self.factorCarga = self.elementos / self.size
		#print (str(self.factorCarga))
		if self.factorCarga > 0.6:
			print("Realizando Rehash! \n La Tabla está llena a más del 50%.")
			tablaH = self.table
			self.rehashing()
			for n in tablaH:
				if n != None:
					#print (str(n.getValor()))
					self.insertarHash(n.getNombre())
		print("|" + str(nodo.getClave()) + "/" + str(nodo.getNombre()) + "--" + str(nodo.getPosicion()) + "|")		

	def insertarHash(self, nombre, desc, direc, hora):
		self.nodo = self.insertar(nombre, desc, direc, hora, self.nodo)
		#print("|" + str(nombre) + "|")

	def mostrarHash(self):
		print ("| Pos  |  Clave  --  Valor  |")
		for nodo in self.table:
			if nodo != None:
				print ("------------------------")
				print ("| " + str(nodo.getPosicion()) + "  |  " + str(nodo.getClave()) + "  --  " + str(nodo.getNombre()) + "  |")

	def buscar(self, nombre):
		posicion = self.obtenerPosicion(nombre)
		#print(posicion)
		if self.table[posicion] != None:
			if self.table[posicion].eliminado == True:
				return None		
		print ("El elemento buscado es: " + str(self.table[posicion].getNombre()) 
			+ " y esta en la posicion: " + str(self.table[posicion].getPosicion()))
		return self.table[posicion]

	def modificar(self, name, desc, direc, hora):
		evento = self.buscar(name)
		if name == evento.getNombre():
			evento.descripcion = desc
			evento.direccion = direc
			evento.hora = hora
			print ("Evento modificado: " + evento.getNombre() + "--" 
				+ evento.getDescripcion() + "--" + evento.getDireccion() + "--" + evento.getHora())

	def eliminar(self, nombre):
		posicion = self.obtenerPosicion(nombre)
		if self.table[posicion] != None:
			self.table[posicion].eliminado = True
			print("Eliminando: " + str(self.table[posicion].getNombre()) 
				+ " que esta en la posicion: " + str(self.table[posicion].getPosicion()))
			self.table[posicion] = None
			
	def rehashing(self):
		self.size = self.size * 2
		self.table = []
		for i in range(self.size):
			self.table.append(None)
		print("Nuevo tamaño: " + str(self.size))

	"""def graficar(self):
		grafo = "digraph G {\n" + "node [shape=plaintext];\n" + "matriz [label=<\n"
		grafo += "TABLE BORDER=\"0\" CELLBORDER=\"1\" CELLSPACING=\"0\" CELLPADDING=\"4\">\n"

		for i in self.table:
			if i != None:
				grafo += "<TR><TD HEIGHT=\"30\" WIDTH=\"80\" FIXEDSIZE =\"TRUE\" BGCOLOR=\"#010179\"><font color=\"red\">" + str(i.getValor()) + "</font></TD></TR> \n"
			#else:
				#grafo += "<TR><TD HEIGHT=\"3\" WIDTH=\"80\" FIXEDSIZE =\"TRUE\" BGCOLOR=\"#BFBFBF\"></TD></TR>\n"

		grafo += "</TABLE>>];\n" +" label=\"TABLA EVENTOS\"}"
		print(grafo)
		
		src = Source(grafo)
		src.format = "png"
		src.render('test-output/TablaHash', view = True)"""

	def graficar(self):
		grafo = "digraph g {\n graph [rankdir=UD];\n node [shape = record,height=.1];  { \n"
		
		i = 0
		for nodo in self.table:
			if nodo != None:
				grafo += "\"" + str(i) + "\" [label = \"" + "Pos: " + str(nodo.getPosicion())
				grafo += "\\nNombre: " + nodo.getNombre() + "\\nDescripcion: " + nodo.getDescripcion() 
				grafo += "\\nDireccion: " + nodo.getDireccion() + "\\nHora: " + nodo.getHora() + "\"];\n"
				if i > 0:
					grafo += "\"" + str(i - 1) + "\" -> \"" + str(i) + "\"[dir=none] ;\n"
				i = i + 1
		grafo += "}  labelloc=\"t\"; label=\" TABLA HASH EVENTOS\";}"
		print(grafo)
		src = Source(grafo)
		src.format = "png"
		src.render('test-output/TablaHash', view = True)