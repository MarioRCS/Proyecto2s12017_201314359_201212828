from graphviz import Source
from .NodoLDU import NodoLDU

class ListaDobleUsuarios(object):
	
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

	def insertarInicio(self, nombre, password):
		nuevo = NodoLDU(self.indice, nombre, password)
		
		if self.estaVacia() == True:
			self.inicio = self.fin = nuevo
		else:
			nuevo.siguiente = self.inicio
			self.inicio.anterior = nuevo
			self.inicio = nuevo

		self.indice += 1

	def insertarFinal(self, nombre, password):
		#if len(password) >= 4:
		nuevo = NodoLDU(self.indice, nombre, password)

		if self.estaVacia() == True:
			self.fin = self.inicio = nuevo
		else:
			nuevo.anterior = self.fin
			self.fin.siguiente = nuevo
			self.fin = nuevo

		self.indice += 1
		#else:
		

	def buscar(self, nombre):
		temp = self.inicio
		encontrado = False

		while temp != None and encontrado != True:
			if temp.getNombre() == nombre:
				encontrado = True
				print("Nombre: " + temp.getNombre() + " encontrado en el indice " + str(temp.getIndice()))
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
				print (temp.getIndice() , "--" , temp.getNombre() , "--" , temp.getPassword())
				temp = temp.siguiente

	def mostrarFinInicio(self):
		if self.estaVacia() == True:
			print ("Lista Vacia")
		else:
			temp = self.fin
			while temp != None:
				print (temp.getIndice() , "--" , temp.getNombre() , "--" , temp.getPassword())
				temp = temp.anterior			

	def eliminarIndice(self, indice):
		if self.inicio != None:
			temp = self.inicio
			temp2 = None
			while temp != self.fin:
				if temp.getIndice() == indice:
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


			if indice == temp.getIndice():
				self.fin = temp.anterior
				self.fin.siguiente = None

	def verificarUsuario(self, nombre, password):
		usuario = self.buscar(nombre)
		if (nombre == usuario.getNombre()) and ( password == usuario.getPassword()):
			print ("Usuario " + usuario.getNombre() + " correcto")
			return True
		else:
			print ("Usuario " + usuario.getNombre() + " incorrecto")
			return False

	def graficar(self):
		self.grafo = "digraph G {\n" + "graph [rankdir = TB];\n" + "node [shape = record,height=.1];  {\n"

		if self.estaVacia() == True:
			self.grafo += "\"ListaVacia\" [label = \"Lista Vacia\"]"
		else:
			temp = self.inicio
			i = 0
			while temp != None:
				self.grafo += "\"" + str(i) + "\" [label = \"" + "Nombre: " + temp.getNombre() 
				self.grafo += "\\nContraseña: " + temp.getPassword() + "\"];\n"
				if i > 0:
					self.grafo +=  "\"" + str(i - 1) + "\" -> \"" + str(i) + "\" ;\n"
					self.grafo +=  "\"" + str(i) + "\" -> \"" + str(i - 1) + "\" ;\n"

				temp = temp.siguiente
				i = i + 1

		self.grafo += "} labelloc=\"t\"; label=\" LISTA DOBLE USUARIOS\";}"
		print(self.grafo)
		src = Source(self.grafo)
		src.format = "png"
		src.render('test-output/ListaDobleUsuarios', view = True)
#**************************************************************************#
#************************* METODOS PARA LA MATRIZ *************************#
	#******************** INSERCIÓN ********************#
	def insertarMatrizLDU(self, nombre, dia, mes, anio, evento, desc, direc, hora) :
		usuario = self.buscar(nombre)
		#print(usuario.getIndice())
		if nombre == usuario.getNombre():
			usuario.insertarMatriz(dia, mes, anio, evento, desc, direc, hora)
			print("Nodo insertado en Lista: " + str(dia) + "--" + mes + "--" + anio)
	#******************** GRAFICAR ********************#
	def graficarMatrizLDU(self, nombre, anio, mes, dia):
		usuario = self.buscar(nombre)
		print(str(usuario.getNombre()))
		if nombre == usuario.getNombre():
			usuario.graficarMatriz()
			usuario.graficarLista(anio, mes)
			usuario.graficarHash(anio, mes, dia)
