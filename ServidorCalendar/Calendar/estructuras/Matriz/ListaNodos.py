from .NodoListaNodos import NodoListaNodos

class ListaNodos(object):

	def __init__(self):
		self.inicio = None
		self.fin = None

	def insertarX(self, nodo):
		if self.inicio == None:
			self.inicio = self.fin = nodo
		else:
			mayor = self.buscarNodoXMayor(nodo.getPosY())
			if mayor == self.inicio:
				nodo.abajo = self.inicio
				self.inicio.arriba = nodo
				self.inicio = nodo
			elif mayor == None:
				self.fin.abajo = nodo
				nodo.arriba = self.fin
				self.fin = nodo
			else:
				mayor.arriba.abajo = nodo
				nodo.arriba = mayor.arriba
				nodo.abajo = mayor
				mayor.arriba = nodo

	def insertarY(self, nodo):
		if self.inicio == None:
			self.inicio = self.fin = nodo
		else:
			mayor = self.buscarNodoYMayor(nodo.getPosX())
			if mayor == self.inicio:
				nodo.derecha = self.inicio
				self.inicio.izquierda = nodo
				self.inicio = nodo
			elif mayor == None:
				self.fin.derecha = nodo
				nodo.izquierda = self.fin
				self.fin = nodo
			else:
				mayor.izquierda.derecha = nodo
				nodo.izquierda = mayor.izquierda
				nodo.derecha = mayor
				mayor.izquierda = nodo

	def buscarNodoXMayor(self, indice):
		temp = self.inicio
		while temp != None:
			if temp.getPosY() > indice:
				return temp
			temp = temp.abajo
		return None

	def buscarNodoYMayor(self, indice):
		temp = self.inicio
		while temp != None:
			if temp.getPosX() > indice:
				return temp
			temp = temp.derecha
		return None