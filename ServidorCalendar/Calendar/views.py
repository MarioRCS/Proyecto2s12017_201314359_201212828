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

	if sesion == "":
		return redirect('/login/')

	return render(request, 'Calendar/calendario.html')

def logout(request):
	global sesion
	sesion = ""
	return redirect('/login/')