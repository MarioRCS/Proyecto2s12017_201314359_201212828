class NodoListaNodos(object):
	def __init__ (self, listaDias):
		self.arriba = None
		self.abajo = None
		self.izquierda = None
		self.derecha = None
		from .NodoIndice import NodoIndice
		self.padreX = None
		self.padreY = None
		self.listaDias = listaDias
		from ListaDobleDias.LDDias import ListaDobleDias
		self.ldDias = ListaDobleDias()


	def getPosX(self):
		return self.padreX.getIndice()

	def getPosY(self):
		return self.padreY.getIndice()

	def agregarDia(self, dia):
		self.listaDias += '--' + dia
	
	def getDia(self):
		return self.listaDias
	
	
#******************** MÉTODOS LD DIAS ********************#
	def insertarLD(self, dia):
		self.ldDias.insetarOrdenado(dia)

	def buscarLD(self, dia):
		dEvento = self.ldDias.buscar(dia)
		return dEvento

	def eliminarLD(self,dia):
		self.ldDias.eliminar(dia)

	def graficarLD(self):
		self.ldDias.graficar()
		#graphAVL = self.avlTree.graficarAVL()
		#return graphAVL
#******************* MÉTODOS TABLA HASH *******************#
	def insertarHashMatriz(self, dia, evento, desc, direc, hora):
		self.ldDias.insertarHashLD(dia, evento, desc, direc, hora)

	def modificarHashMatriz(self, dia, name, desc, direc, hora):
		self.ldDias.modificarHashLD(dia, name, desc, direc, hora)

	def graficarHashMatriz(self, dia):
		self.ldDias.graficarHashLD(dia)