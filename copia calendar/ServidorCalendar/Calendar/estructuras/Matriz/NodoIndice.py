from .ListaNodos import ListaNodos

class NodoIndice(object):
	def __init__ (self, indice):
		self.indice = indice
		self.siguiente = None
		self.anterior = None
		self.listaNodos = ListaNodos()

	def getIndice(self):
		return self.indice
