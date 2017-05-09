class NodoLDU(object):
	def __init__ (self, indice, nombre, password):
		self.indice = indice
		self.nombre = nombre
		self.password = password
		self.anterior = None
		self.siguiente = None
		from ..Matriz.Matriz import Matriz
		self.matrizD = Matriz()

	def getIndice(self):
		return self.indice

	def getNombre(self):
		return self.nombre

	def getPassword(self):
		return self.password

#******************** MÉTODOS MATRIZ ********************#
	def insertarMatriz(self, dia, mes, anio, evento, desc, direc, hora):
		self.matrizD.insertar(dia, mes, anio, evento, desc, direc, hora)

	def eliminarMatriz(self, anio, mes, dia, evento):
		self.matrizD.eliminarHashMatriz(anio, mes, dia, evento)

	def graficarMatriz(self):
		self.matrizD.graficar()

	def graficarLista(self, anio, mes):
		self.matrizD.graficarLDMatriz(anio, mes)

	def graficarHash(self, anio, mes, dia):
		self.matrizD.graficarHashMatriz(anio, mes, dia)