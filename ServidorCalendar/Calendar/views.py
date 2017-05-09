from django.http import HttpResponse
from django.shortcuts import render, redirect

#************ IMPORTACIONES DE CLASES ************#
from .estructuras.ListaDobleUsuarios.LDUsuarios import ListaDobleUsuarios
#*************************************************#

#*********** INSTANCIAMIENTO DE CLASES ***********#
ldU = ListaDobleUsuarios()
#*************************************************#

global sesion
sesion = ""

def registro(request):
    return render(request, 'Calendar/registro.html')

def registrar(request):
	if request.method == 'POST':
		user = request.POST.get('usuario')
		password = request.POST.get('password')
		mensaje = "Registrado con Exito!"
		error = "Contraseña no valida. Debe ser al menos de 4 caracteres"

		if len(password) >= 4:
			ldU.insertarFinal(str(user), str(password))
		else:
			return render(request, 'Calendar/registro.html', {'error': error})
		
		ldU.graficar()

	return render(request, 'Calendar/registro.html', {'mensaje': mensaje})

def login(request):
    return render(request, 'Calendar/login.html')

def validacion(request):
	if request.method == 'POST':
		user = request.POST.get('usuario')
		password = request.POST.get('password')
		error = "Usuario Incorrecto!"

		if ldU.verificarUsuario(str(user), str(password)) == True:
			global sesion
			sesion = user
			return redirect('/calendario/')
		else:
			return render(request, 'Calendar/login.html', {'error': error})

def calendario(request):
	global sesion
	mes = request.POST.get('mes')
	anio = request.POST.get('anio')

	if sesion == "":
		return redirect('/login/') 

	usuario = ldU.buscar(sesion)
	matriz = usuario.matrizD
	nodoInterno = matriz.buscar(anio, mes)
	deventos = []
	dias = []
	if request.method == 'POST':
		if nodoInterno != None:
			listaDoble = nodoInterno.ldDias
			temp = listaDoble.inicio
			while temp != None:
				dias.append(temp.dia)
				tablaHash = temp.hash 
				temp2 = tablaHash.table
				eventos = []
				for evento in temp2:
					if evento != None:
						eventos.append(evento.nombre)
						print("evento: " + str(evento.nombre))
						print(eventos)
				deventos.append(eventos)
				temp = temp.siguiente

	return render(request, 'Calendar/calendario.html', {'dias': dias, 'eventos': deventos})

def evento(request):
	return render(request, 'Calendar/evento.html')

def creacion(request):
	global sesion

	if request.method == 'POST':
		mensaje = "Evento creado con Exito!"
		name = request.POST.get('nombre')
		adress = request.POST.get('direccion')
		desc = request.POST.get('descripcion')
		time = request.POST.get('hora')
		day = request.POST.get('dia')
		month = request.POST.get('mes')
		year = request.POST.get('anio')

		print(sesion)
		ldU.insertarMatrizLDU(str(sesion), int(day), str(month), str(year), str(name), str(desc), str(adress), str(time))
				
		ldU.graficarMatrizLDU(sesion, str(year), str(month), int(day))

	return render(request, 'Calendar/evento.html', {'mensaje': mensaje})

def eliminar(request):
	global sesion

	if request.method == 'POST':
		mensaje = "Evento eliminado!"
		name = request.POST.get('evento')
		day = request.POST.get('dia')
		month = request.POST.get('mes')
		year = request.POST.get('anio')
		
		print(sesion + "--" + year + "--" + month + "--" + day + "--" + name)
		ldU.eliminarMatrizLDU(str(sesion), str(year), str(month), int(day), str(name))
	return render(request, 'Calendar/calendario.html', {'mensaje': mensaje})

def logout(request):
	global sesion
	sesion = ""
	return redirect('/login/')

