class NodoTH(object):
	def __init__ (self, clave, nombre, descripcion, direccion, hora, posicion):
		self.clave = clave
		self.nombre = nombre
		self.descripcion = descripcion
		self.direccion = direccion
		self.hora = hora
		self.posicion = posicion			
		self.eliminado = False

	def getClave(self):
		return self.clave

	def getNombre(self):
		return self.nombre

	def getDescripcion(self):
		return self.descripcion

	def getDireccion(self):
		return self.direccion

	def getHora(self):
		return self.hora

	def getPosicion(self):
		return self.posicion