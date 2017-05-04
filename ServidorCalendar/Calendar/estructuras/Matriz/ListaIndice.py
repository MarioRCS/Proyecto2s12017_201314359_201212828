from .NodoIndice import NodoIndice

class ListaIndice(object):

	def __init__(self):
		self.inicio = None
		self.fin = None

	def insertarIndice(self, nodo):
		if self.inicio == None:
			self.inicio = self.fin = nodo
		else:
			mayor = self.buscarMayor(nodo.getIndice())
			if mayor == self.inicio:
				nodo.siguiente = self.inicio
				self.inicio.anterior = nodo
				self.inicio = nodo
			elif mayor == None:
				self.fin.siguiente = nodo
				nodo.anterior = self.fin
				self.fin = nodo
			else:
				mayor.anterior.siguiente = nodo
				nodo.anterior = mayor.anterior
				nodo.siguiente = mayor
				mayor.anterior = nodo

	def buscarMayor(self, indice):
		temp = self.inicio
		while temp != None:
			if temp.getIndice() > indice:
				return temp
			temp = temp.siguiente
		return None

	def buscar(self, indice):
		temp = self.inicio
		while temp != None:
			if temp.getIndice() == indice:
				return temp
			temp = temp.siguiente
		return None