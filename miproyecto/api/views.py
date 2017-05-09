from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf   import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from api.ArbolB import ArbolB
from api.AVL import Arbol,NodoArbol

@csrf_exempt
@csrf_protect
@ensure_csrf_cookie

class metodos:

        global ar

        global  numi
        ar=ArbolB()
        numi=0
        
        def prueba(request,dato1,dato2):
                param1=str(dato1)
                param2=str(dato2)
                dato=int(numi)+1
                ar.InsertarBitacora("Intento Login"+param1,dato)
                if ar.Login(param1,param2):
                        return HttpResponse("true")
                else:
                        return HttpResponse("datos incorrectos")

        def Insertarusuario(request,dato3,dato4):
                parametro1=str(dato3)
                parametro2=str(dato4)
                numi=int(numi)+1
                ar.InsertarBitacora("Usuario Registrado"+parametro1,numi)
                ar.InsertarUsuario(parametro1,parametro2)
                return HttpResponse("Usuario Ingresado Exitosamente")

        def Graficarlista(request):
                texto=""
                texto=str(ar.GraficarLista())
                return  HttpResponse(texto)

        def ActualizarCarpeta(request,dato1):
                ruta=""
                ruta=str(dato1)
                respuesta=""
                respuesta= ar.ActualizarCarpetaenRuta(ruta)
                return HttpResponse(respuesta)

        def CrearCarpeta(request,dato1,dato2):
                dato=int(numi)+1
                ar.InsertarBitacora("Creacion Carpeta"+str(dato2),dato)
                ar.CarpetaEnRuta(dato1,dato2)
                
                return HttpResponse("Carpeta Creada Exitosamente")


        def GraficarArbolB(request,dato1):
                ruta = str(dato1)
                ar.textoB=""
                respuesta="digraph g{\n"+'rankdir = "'+"UD"+'"\n'
                respuesta += ar.GraficarBenRuta(ruta)
                respuesta+="\n}"
                return HttpResponse(respuesta)

        def SubirArchivo(request,dato1,dato2,dato3):
                dato=int(numi)+1
                ar.InsertarBitacora("Subida de Archivo"+str(dato2),dato)
                param1=str(dato1)
                param2=str(dato2)
                param3=str(dato3)

                ar.ArchivoEnRuta(dato1,dato2,dato3)
                return HttpResponse("Archivo Subido Exitosamente")

        def GraficarAvl(request,dato1):
                ruta=str(dato1)
                respuesta=""
                respuesta= ar.AvlEnRuta(ruta)
                respuesta+="\n}"
                return HttpResponse(respuesta)


        def ActualizarA(request,dato1):
                ruta= str(dato1)
                respuesta=""
                respuesta= ar.ActualizarArchivos(ruta)
                return HttpResponse(respuesta)

        def DescargarArchivo(request,dato1,dato2):
                ruta=str(dato1)
                archivo=str(dato2)
                dato=int(numi)+1
                ar.InsertarBitacora("DescargaArchivo"+archivo,dato)
                bits=ar.GetBits(ruta,archivo)
                return HttpResponse(bits)

        def EliminarCarpeta(request,dato1,dato2):
                ruta=str(dato1)
                carpeta=str(dato2)
                dato=int(numi)+1
                ar.InsertarBitacora("Eliminar Carpeta"+carpeta,dato)
                ar.EliminarBenRuta(ruta,carpeta)

                return HttpResponse("La Carpeta Fue Eliminada Correctamente")

        def EliminarArchivo(request,dato1,dato2):
                ruta = str(dato1)
                archivo=str(dato2)
                dato=int(numi)+1
                ar.InsertarBitacora("Eliminar Archivo"+archivo,dato)
                ar.EliminarAvlRuta(ruta,archivo)
                return HttpResponse("El archivo fue eliminado Correctamente")

        def ModificarCarpeta(request,dato1,dato2,dato3):
                ruta=str(dato1)
                nombreviejo=str(dato2)
                nombrenuevo=str(dato3)
                dato=int(numi)+1
                ar.InsertarBitacora("Modificar Carpeta"+nombreviejo,dato)
                ar.ModificarBenRuta(ruta,nombreviejo,nombrenuevo)
                return HttpResponse("La carpeta fue modificada Correctamente")

        def ModificarArchivo(request,dato1,dato2,dato3):
                ruta = str(dato1)
                nombreviejo=str(dato2)
                nombrenuevo=str(dato3)
                dato=int(numi)+1
                ar.InsertarBitacora("Modificar Archivo"+nombreviejo,dato)
                ar.ModificarArchivoRuta(ruta,nombreviejo,nombrenuevo)
                return HttpResponse("El archivo fue modificado Correctamente")

        def GraficarBitac(request):
                respuesta=(ar.GraficarBitacora())
                respuesta+="\n}"
                return HttpResponse(respuesta)







# Create your views here.
