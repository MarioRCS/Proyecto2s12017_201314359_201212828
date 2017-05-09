class NodoLDD(object):
	def __init__ (self, indice, dia):
		self.indice = indice
		self.dia = dia
		self.anterior = None
		self.siguiente = None
		from ..TablaHash.Hash import TablaHash
		self.hash = TablaHash()

	def getIndice(self):
		return self.indice

	def getDia(self):
		return self.dia

#****************** MÉTODOS TABLA HASH ******************#
	def insertarHash(self, nombre, desc, direc, hora):
		self.hash.insertarHash(nombre, desc, direc, hora)

	def modificarHash(self, name, desc, direc, hora):
		self.hash.modificar(name, desc, direc, hora)

	def eliminarHash(self,nombre):
		self.hash.eliminar(nombre)

	def graficarHash(self):
		self.hash.graficar()
		#graphAVL = self.avlTree.graficarAVL()
		#return graphAVL